
"""
Funções para facilitar a implementação de um ETL, subindo o nível de abstração
para um job de carga de dados.

Se parâmetro '-v' (de verbose) for passado na linha de comando ao executar o
script de carga, a quantidade de registros lidos e gravados será impressa no
console.
"""

import sys
from datetime import datetime

import blipy.tabela_entrada as te
import blipy.tabela_saida as ts
import blipy.func_transformacao as ft

from enum import Enum, auto
from blipy.planilha import Planilha
from blipy.arquivo_csv import ArquivoCSV
from blipy.tabela_html import TabelaHTML
from blipy.enum_tipo_col_bd import TpColBD as tp


# Tipos de estratégias de gravação no banco
class TpEstrategia(Enum):
    # deleta todas as linhas da tabela antes de inserir as novas linhas
    DELETE = auto()    

    # simplesmente insere as novas linhas
    INSERT = auto()    

    # trunca a tabela antes de inserir as novas linhas
    TRUNCATE = auto()    


    # Quando a estratégia UPDATE_INSERT ou INSERT_UPDATE é utilizada, a técnica
    # de realizar várias gravações simultaneamente no banco (atributo
    # __qtd_insercoes_simultaneas de Job) é ignorada quando o registro é
    # atualizado (ou seja, sempre vai ser atualizado um registro de cada vez),
    # mas ainda é válida no caso das inserções

    # Primeiro tenta atualizar o registro, e se não conseguir, o insere.
    UPDATE_INSERT = auto()

    # Primeiro tenta inserir o registro, e se ele já existir, o atualiza.
    INSERT_UPDATE = auto()

    # Quando a estratégia UPDATE é utilizada, a técnica de realizar várias
    # gravações simultaneamente no banco (atributo __qtd_insercoes_simultaneas
    # de Job) não é utilizada, ou seja, a atualização é sempre feita um
    # registro por vez
    UPDATE = auto()


class Job():
    def __init__(self, nome_job):
        self.__verbose = False
        if len(sys.argv) > 1:
            if sys.argv[1] == "-v":
                self.__verbose = True
 
        self.__nome = nome_job
 
        print()
        print("====== Job " + self.__nome + " iniciado " + "=======")
        print("-----> Horário de início:  " +  \
                str(datetime.now().replace(microsecond=0)))

        # por padrão, vai usar o valor default de TabelaSaida
        self.__qtd_insercoes_simultaneas = None

        self.__reset_func_pre_pos_processamento()

    def __del__(self):
        print("====== Job " + self.__nome + " finalizado " + "=====")
        print("-----> Horário de término: " +  \
                str(datetime.now().replace(microsecond=0)))

    @property
    def qtd_insercoes_simultaneas(self):
        return self.__qtd_insercoes_simultaneas
    @qtd_insercoes_simultaneas.setter
    def qtd_insercoes_simultaneas(self, qtd_insercoes_simultaneas):
        self.__qtd_insercoes_simultaneas = qtd_insercoes_simultaneas

    def __reset_func_pre_pos_processamento(self):
        """
        Configura as funções de pré e pós processamento de cada registro para
        seus valores default, ou seja, retornam sempre True
        """
        self.__funcao_pre_processamento = lambda _: True
        self.__funcao_pos_processamento = lambda _, __: True

    def set_func_pre_processamento(self, funcao):
        """
        Seta a função que será chamada antes do processamento de cada linha dos
        dados de entrada. A função deverá ter como parâmetro uma tupla, que
        receberá o registro lido dos dados de entrada. Esta função deverá
        retornar True se o processamento do registro deve continuar ou False
        para pular esse registro e ir para o próximo registro de entrada.

        Ao final do processamento de carga de uma tabela, esta função é
        resetada para seu valor default, ou seja, retorna sempre True.
        """
        self.__funcao_pre_processamento = funcao

    def set_func_pos_processamento(self, funcao):
        """
        Seta a função que será chamada após o processamento de cada linha dos
        dados de entrada. A função deverá ter como parâmetros duas tuplas, uma 
        que receberá o registro original dos dados de entrada e outra que
        conterá o registro que foi efeitvamente gravado no banco, ou seja, após
        qualquer transformação porventura feita no dado de entrada. O retorno
        desta função atualmente é ignorado.

        Ao final do processamento de carga de uma tabela, esta função é
        resetada para seu valor default, ou seja, retorna sempre True.
        """
        self.__funcao_pos_processamento = funcao

    def grava_log_atualizacao(self, 
            conexao,
            tabela_log="LOG_ATUALIZACAO"):
        """
        Grava na tabela de log a data da última atualização dos dados. O nome
        da tabela de log é LOG_ATUALIZACAO por padrão, mas pode ser alterado. O
        nome do campo com a data da última atualização é sempre
        DT_ULT_ATUALIZACAO.

        Args:
        conexao:    conexão do esquema no banco onde está a tabela de log
        tabela_log: nome da tabela de log
        """

        ret = conexao.executa(
            "update " + tabela_log + 
            " set dt_ult_atualizacao = sysdate")

        if ret.rowcount == 0:
            # é a primeira vez que o log é gravado, tanta então um insert
            conexao.executa(
                "insert into " + tabela_log + " (dt_ult_atualizacao)"
                "  values (sysdate)")

    def importa_tabela_por_sql(self, conn_entrada, conn_saida, sql_entrada,
            nome_tabela_saida, cols_saida, estrategia=TpEstrategia.DELETE,
            cols_chave_update=None):
        """
        Importação do resultado de uma consulta sql para o banco de dados. A
        tabela de destino por default é limpa e carregada de novo (considera-se
        que são poucas linhas), mas isso pode ser alterado pelo parâmetro
        "estrategia". Qualquer erro dispara uma exceção.

        Args:
        conn_entrada:   conexão com o esquema de entrada de dados (geralmente
                        o staging)
        conn_saida:     conexão com o esqumea de saída (geralmente a produção)
        sql_entrada:    consulta sql que irá gerar os dados de entrada
        nome_tabela_saida: nome da tabela de saida
        cols_saida:     lista das colunas que serão gravadas na tabela de
                        saida, com o nome da coluna, seu tipo e a função de
                        transformanção a ser aplicada (função de transformação
                        é opcional; se não informado, faz só uma cópia do dado)
        estrategia:     estratégia de gravação que será utilizada (enum
                        TpEstrategia)
        cols_chave_update:  lista com os nomes das colunas que serão chave de
                            um eventual update na tabela. Esse parâmetro só faz
                            sentido para se parâmetro
                            estrategia=TpEstrategia.UPDATE_INSERT ou
                            INSERT_UPDATE ou UPDATE e é obrigatório nestes
                            casos. Essas colunas também têm que fazer parte do
                            parâmetro cols_saida
        """

        tab_entrada = te.TabelaEntrada(conn_entrada)
        tab_entrada.carrega_dados(sql_entrada)

        self.__grava_tabela(    tab_entrada, 
                                conn_saida, 
                                nome_tabela_saida, 
                                cols_saida, 
                                estrategia, 
                                cols_chave_update)

    def importa_tabela_por_nome(self, conn_entrada, conn_saida, 
            nome_tabela_entrada, nome_tabela_saida, cols_entrada, cols_saida,
            filtro_entrada="", estrategia=TpEstrategia.DELETE, 
            cols_chave_update=None):
        """
        Importação de uma tabela para o banco de dados. A tabela de destino por
        default é limpa e carregada de novo (considera-se que são poucas
        linhas), mas isso pode ser alterado pelo parâmetro "estrategia".
        Qualquer erro dispara uma exceção.

        Args:
        conn_entrada:       conexão com o esquema de entrada de dados
                            (geralmente o staging)
        conn_saida:         conexão com o esqumea de saída (geralmente a
                            produção)
        nome_tabela_entrada: nome da tabela de entrada
        nome_tabela_saida:  nome da tabela de saida
        cols_entrada:       lista dos nomes das colunas que serão buscadas na
                            tabela de entrada
        cols_saida:         lista das colunas que serão gravadas na tabela de
                            saida, com o nome da coluna, seu tipo e a função de
                            transformanção a ser aplicada (função de
                            transformação é opcional; se não informado, faz só
                            uma cópia do dado)
        filtro_entrada:     filtro opcional dos registros da tabela de entrada,
                            no formato de uma cláusula WHERE de SQL, sem a
                            palavra WHERE
        estrategia:         estratégia de gravação que será utilizada (enum
                            TpEstrategia)
        cols_chave_update:  lista com os nomes das colunas que serão chave de
                            um eventual update na tabela. Esse parâmetro só faz
                            sentido para se parâmetro
                            estrategia=TpEstrategia.UPDATE_INSERT ou
                            INSERT_UPDATE ou UPDATE e é obrigatório nestes
                            casos. Essas colunas também têm que fazer parte do
                            parâmetro cols_saida

        Obs.:
        Para calcular o valor de saída baseado em mais de uma coluna de um
        mesmo registro da tabela de entrada, colocar as colunas numa lista
        dentro da lista cols_entrada. Por exemplo:

        cols_entrada = ["ID_CHAVE",
                        "QT_VALOR1",
                        "QT_VALOR2",
                        ["QT_VALOR1", "QT_VALOR2"]]
        cols_saida = [ ["ID_CHAVE", tp.NUMBER],
                       ["QT_VALOR1", tp.NUMBER],
                       ["QT_VALOR2", tp.NUMBER],
                       ["QT_SOMATORIO", tp.NUMBER, ft.Somatorio()]]

        QT_SOMATORIO na tabela de saída vai ser o resultado da aplicação de
        ft.Somatorio() nos valores das colunas QT_VALOR1 e QT_VALOR2 da tabela
        de entrada, registro a registro.
        """

        # salva no parâmetro que vai ser passsdo pra __grava_tabela quantas
        # colunas de entrada serão usadas no cálculo do valor de cada coluna de
        # saída, se for o caso de se usar a sintaxe "col1, col2, col_n" em
        # algum item de cols_entrada
        i = 0
        cols = []
        for col in cols_entrada:
            if isinstance(col, list):
                for c in col:
                    cols.append(c)
                qtd_colunas = len(col)
                cols_saida[i].append(qtd_colunas)
            else:
                cols.append(col)
                qtd_colunas = 1

            if qtd_colunas > 1:
                cols_saida[i].append(qtd_colunas)
            i += 1

        tab_entrada = te.TabelaEntrada(conn_entrada)
        tab_entrada.carrega_dados(
                nome_tabela_entrada, 
                cols, 
                filtro=filtro_entrada)

        self.__grava_tabela(    tab_entrada, 
                                conn_saida, 
                                nome_tabela_saida, 
                                cols_saida, 
                                estrategia,
                                cols_chave_update)

    def importa_planilha(self, 
            conn_saida, 
            nome_tab_saida, 
            cols_saida, 
            io, sheet_name=0, header=0, skipfooter=0, 
            names=None, index_col=None, usecols=None,
            skiprows=None, nrows=None, na_values=None, engine='openpyxl',
            thousands=None, cols_entrada=None, tp_cols_entrada=None,
            estrategia=TpEstrategia.DELETE,
            cols_chave_update=None):
        """
        Importação de uma tabela para o banco de dados. A tabela de destino por
        default é limpa e carregada de novo (considera-se que são poucas
        linhas), mas isso pode ser alterado pelo parâmetro "estrategia".
        Qualquer erro dispara uma exceção.

        Args:
        conn_saida:     conexão com o esqumea de saída (geralmente a produção)
        nome_tab_saida: nome da tabela de saida
        cols_saida:     lista das colunas que serão gravadas na tabela de
                        saida, com o nome da coluna, seu tipo e a função de
                        transformanção a ser aplicada (funão de transformação é
                        opcional; se não informado, faz só uma cópia do dado)
        io:             caminho (path) da planilha, com nome da planilha
                        incluso ou uma URL
        sheet_name:     aba ou guia do Excel, pode ser o nome ou número
                        0-indexed
        header:         linhas de cabeçalho a serem ignoradas, 0-indexed
        skipfooter:     linhas de rodapé (final arquivo) a serem ignoradas,
                        0-indexed.
        names:          lista de nomes de colunas. Se arquivo não contém
                        header, deve-se obrigatoriamente setar header=None
        index_col:      coluna a ser usada como label das linhas
        usecols:        seleção de colunas. Tipos de seleção: 'A,B,C',
                        [0,1,2], ['ID','Coluna_1','Coluna_4']
        skiprows:       linhas a serem ignoradas no início do arquivo,
                        0-indexed
        nrows:          número de linhas a serem carregadas
        na_values:      lista de strings a serem consideradas como dados
                        não disponívels (NaN)
        engine:         o padrão é openpyxl. Existem outras para formatos
                        antigos ex .odf
        thousands:      separador de milhar
        cols_entrada:   lista com o índice (zero-based) das colunas lidas que 
                        serão utilizadas. Se None, utiliza todas as
                        colunas, na ordem lida. Esse parâmetro é
                        importante quando se quer que uma única coluna da
                        planilha seja fonte de entrada para mais de uma coluna
                        de saída, já que a relação entre cols_saida e
                        cols_entrada tem que ser de 1 para 1.  Por exemplo, se
                        a primeira coluna da planilha for fonte de entrada para
                        a primeira e terceira colunas da tabela de saída, esse
                        parâmetro deve ser [0, 1, 0]
        tp_cols_entrada tipos das colunas de entrada na planilha, no formato
                        de um array de objetos TpColBD, na ordem das colunas da
                        planilha ou do parâmetro usecols. Se não informado,
                        os tipos são obtidos a partir do parâmetro cols_saida
                        (no caso de não se usar o parâmetro usecols) ou o
                        pandas tentará obtê-los automaticamente (se usecols for
                        usado)
        estrategia:     estratégia de gravação que será utilizada (enum
                        TpEstrategia)
        cols_chave_update:  lista com os nomes das colunas que serão chave de
                            um eventual update na tabela. Esse parâmetro só faz
                            sentido para se parâmetro
                            estrategia=TpEstrategia.UPDATE_INSERT ou
                            INSERT_UPDATE ou UPDATE e é obrigatório nestes
                            casos. Essas colunas também têm que fazer parte do
                            parâmetro cols_saida

        Obs.: os argumentos de io a engine são os mesmos do método read_excel
        do Pandas.
        """

        # determina o tipo de cada coluna para a leitura do arquivo pelo pandas
        dtype = self.__monta_dtype(cols_saida, usecols, tp_cols_entrada)

        planilha = Planilha()
        planilha.carrega_dados(io, sheet_name, header, skipfooter, names, 
            index_col, usecols, skiprows, nrows, na_values, engine, thousands,
            dtype)

        if cols_entrada is not None:
            planilha.formata_colunas(cols_entrada)

        self.__grava_tabela(planilha, 
                            conn_saida, 
                            nome_tab_saida, 
                            cols_saida, 
                            estrategia,
                            cols_chave_update)

    def importa_arquivo_csv(self, 
            conn_saida, 
            nome_tab_saida, 
            cols_saida, 
            arquivo, header=0, skipfooter=0, 
            names=None, index_col=None, usecols=None,
            skiprows=None, nrows=None, na_values=None, engine=None,
            sep=";", decimal=".", thousands=None,
            encoding=None, 
            cols_entrada=None, tp_cols_entrada=None,
            estrategia=TpEstrategia.DELETE,
            cols_chave_update=None):
        """
        Importação de uma tabela para o banco de dados. Por default, a tabela
        de destino por default é limpa e carregada de novo (considera-se que
        são poucas linhas), mas isso pode ser alterado pelo parâmetro
        "estrategia". Qualquer erro dispara uma exceção.

        Args:
        conn_saida:     conexão com o esqumea de saída (geralmente a produção)
        nome_tab_saida: nome da tabela de saida
        cols_saida:     lista das colunas que serão gravadas na tabela de
                        saida, com o nome da coluna, seu tipo e a função de
                        transformanção a ser aplicada (funão de transformação é
                        opcional; se não informado, faz só uma cópia do dado)
        arquivo:        caminho (path) do arquivo csv
        header:         linhas de cabeçalho a serem ignoradas, 0-indexed
        skipfooter:     linhas de rodapé (final arquivo) a serem ignoradas,
                        0-indexed.
        names:          lista de nomes de colunas. Se arquivo não contém
                        header, deve-se obrigatoriamente setar header=None
        index_col:      coluna a ser usada como label das linhas
        usecols:        seleção de colunas. Tipos de seleção: 'A,B,C',
                        [0,1,2], ['ID','Coluna_1','Coluna_4']
        skiprows:       linhas a serem ignoradas no início do arquivo,
                        0-indexed
        nrows:          número de linhas a serem carregadas
        na_values:      lista de strings a serem consideradas como dados
                        não disponívels (NaN)
        engine:         engine a ser utilizado
        sep:            caractere separador das células
        decimal:        separador de decimais
        thousands:      separador de milhar
        encoding:       string com o encoding do arquivo csv
        cols_entrada:   lista com o índice (zero-based) das colunas lidas que
                        serão utilizadas. Se None, utiliza todas as
                        colunas, na ordem lida. Esse parâmetro é
                        importante quando se quer que uma única coluna do
                        arquivo seja fonte de entrada para mais de uma coluna
                        de saída, já que a relação entre cols_saida e
                        cols_entrada tem que ser de 1 para 1.  Por exemplo, se
                        a primeira coluna do arquivo for fonte de entrada para
                        a primeira e terceira colunas da tabela de saída, esse
                        parâmetro deve ser [0, 1, 0]
        tp_cols_entrada tipos das colunas de entrada no arquivo CSV, no formato
                        de um array de objetos TpColBD, na ordem das colunas do
                        arquivo CSV ou do parâmetro usecols. Se não informado,
                        os tipos são obtidos a partir do parâmetro cols_saida
                        (no caso de não se usar o parâmetro usecols) ou o
                        pandas tentará obtê-los automaticamente (se usecols for
                        usado)
        estrategia:     estratégia de gravação que será utilizada (enum
                        TpEstrategia)
        cols_chave_update:  lista com os nomes das colunas que serão chave de
                            um eventual update na tabela. Esse parâmetro só faz
                            sentido para se parâmetro
                            estrategia=TpEstrategia.UPDATE_INSERT ou
                            INSERT_UPDATE ou UPDATE e é obrigatório nestes
                            casos. Essas colunas também têm que fazer parte do
                            parâmetro cols_saida

        Obs.: os argumentos de io a engine são os mesmos do método read_csv
        do Pandas.
        """

        # determina o tipo de cada coluna para a leitura do arquivo pelo pandas
        dtype = self.__monta_dtype(cols_saida, usecols, tp_cols_entrada)

        arq_csv = ArquivoCSV()
        arq_csv.carrega_dados(arquivo, header, skipfooter, names, 
            index_col, usecols, skiprows, nrows, na_values, engine, 
            sep, decimal, thousands, dtype, encoding)

        if cols_entrada is not None:
            arq_csv.formata_colunas(cols_entrada)

        self.__grava_tabela(arq_csv, 
                            conn_saida, 
                            nome_tab_saida, 
                            cols_saida, 
                            estrategia,
                            cols_chave_update)

    def importa_tabela_url(self, 
            conn_saida, 
            nome_tab_saida, 
            cols_saida,
            url,
            tabela=0,
            drop=0,
            decimal=",", 
            thousands=".",
            cols_entrada=None, 
            estrategia=TpEstrategia.DELETE):

        """
        Importação para o banco de dados de uma tabela em HTML disponível em
        uma URL . A tabela de destino por default é limpa e carregada de novo 
        (considera-se que são poucas linhas), mas isso pode ser alterado pelo
        parâmetro "estrategia". Qualquer erro dispara uma exceção.

        Args:
        conn_saida:     conexão com o esqumea de saída (geralmente a produção)
        nome_tab_saida: nome da tabela de saida
        cols_saida:     lista das colunas que serão gravadas na tabela de
                        saida, com o nome da coluna, seu tipo e a função de
                        transformanção a ser aplicada (funão de transformação é
                        opcional; se não informado, faz só uma cópia do dado)
        url:            a URL de onde a tabela será lida
        tabela:         qual tabela será lida da URL, no caso de haver mais de
                        uma na mesma página. Zero-based
        drop:           quantos cabeçalhos serão dropados na tabela lida
        decimal:        o indicador de separador decimal usado na tabela lida
        thousands:      o indicador de separador de milhar usado na tabela lida
        cols_entrada:   lista com o índice (zero-based) das colunas lidas que 
                        serão utilizadas. Se None, utiliza todas as
                        colunas, na ordem lida. Esse parâmetro é
                        importante quando se quer que uma única coluna da
                        planilha seja fonte de entrada para mais de uma coluna
                        de saída, já que a relação entre cols_saida e
                        cols_entrada tem que ser de 1 para 1.  Por exemplo, se
                        a primeira coluna da planilha for fonte de entrada para
                        a primeira e terceira colunas da tabela de saída, esse
                        parâmetro deve ser [0, 1, 0]
        estrategia:     estratégia de gravação que será utilizada (enum
                        TpEstrategia)
        """

        tabela_entrada = TabelaHTML()
        tabela_entrada.carrega_dados(url, tabela, drop, decimal, thousands)

        if cols_entrada is not None:
            tabela_entrada.formata_colunas(cols_entrada)

        self.__grava_tabela(tabela_entrada, 
                            conn_saida, 
                            nome_tab_saida, 
                            cols_saida, 
                            estrategia)

    def importa_valores(self, 
        conn_saida, 
        nome_tab_saida, 
        cols_saida, 
        dados_entrada,
        estrategia=TpEstrategia.DELETE):
    
        """
        Salva um conjunto de valores numa tabela do banco. Esses valores estão
        na forma de uma lista de tuplas, cada tupla sendo um registro a ser
        gravado.

        Args:
        conn_saida:     conexão com o esqumea de saída (geralmente a produção)
        nome_tab_saida: nome da tabela de saida
        cols_saida:     lista com o nome das colunas na tabela de saída e seus
                        tipos, conforme os tipos definidos em TpColBD, por
                        exemplo:
                        cols_saida = [["ID_GRUPO_FONTE", tp.NUMBER],
                                      ["NO_GRUPO_FONTE", tp.STRING]]
        dados_entrada:  lista de tuplas com os valores a serem gravados no
                        banco, por exemplo:
                        dados_entrada = [
                            (1, "Recursos do Tesouro-Exercício Corrente"), 
                            (2, "Recursos de Outras Fontes-Exercício Corrente")]
        estrategia:     estratégia de gravação que será utilizada (enum
                        TpEstrategia)
        """

        # monta as colunas de saída
        col = {}
        i = 0
        for _ in cols_saida:
            col[cols_saida[i][0]] =    \
                ts.Coluna(cols_saida[i][0], cols_saida[i][1], ft.f_copia)
            i += 1

        # configura a tabela de saída
        tabela_saida = ts.TabelaSaida(nome_tab_saida, col, conn_saida)

        if estrategia == TpEstrategia.DELETE:
            conn_saida.apaga_registros(nome_tab_saida)
        elif estrategia == TpEstrategia.TRUNCATE:
            conn_saida.trunca_tabela(nome_tab_saida)
        elif estrategia == TpEstrategia.INSERT:
            pass

        # estrategias UPDATE_INSERT, INSERT_UPDATE ou UPDATE não fazem muito
        # sentido aqui, pois a ideia desse método é inserir poucas linhas
        # em tabelas de domínio, então quando se quiser atualizar algum
        # valor é mais prático limpar tudo e carregar novamente (estratégias
        # DELETE ou TRUNCATE)
        elif estrategia == TpEstrategia.UPDATE_INSERT:
            raise NotImplementedError
        elif estrategia == TpEstrategia.INSERT_UPDATE:
            raise NotImplementedError
        elif estrategia == TpEstrategia.UPDATE:
            raise NotImplementedError

        else:
            raise NotImplementedError

        # loop de leitura e gravação dos dados
        qtd_registros = 0
        for r in dados_entrada:
            i = 0
            for c in cols_saida:
                tabela_saida.col[c[0]].calcula_valor( (r[i],) )
                i += 1

            tabela_saida.insere_registro()
            qtd_registros += 1

        if self.__verbose:
            print(  str(qtd_registros) +  \
                    " \tregistros salvos na tabela " +  \
                    nome_tab_saida)

    def __grava_tabela(self, 
            entrada, 
            conn_saida, 
            nome_tabela_saida, 
            cols_saida, 
            estrategia,
            cols_chave_update=None):
        """
        Grava uma tabela no banco de dados.

        Args:
        entrada:            a fonte de entrada dos dados (tabela de banco,
                            planilha etc.)
        conn_saida:         conexão com o esqumea de saída (geralmente a
                            produção)
        nome_tabela_saida:  nome da tabela de saida
        cols_saida:         lista das colunas que serão gravadas na tabela de
                            saida, com o nome da coluna, seu tipo, a função de
                            transformanção a ser aplicada (opcional; se não
                            informado, faz só uma cópia do dado) e a quantidade
                            de colunas de entrada que serão usadas na
                            transformação, se for mais de uma
        estrategia:         estratégia de gravação que será utilizada (enum
                            TpEstrategia)
        cols_chave_update:  lista com os nomes das colunas que serão
                            chave de um eventual update na tabela
        """

        cols = {}
        qtd_colunas_calculo = {}
        for item in cols_saida:
            if len(item) == 2:
                # função de transformanção não informada, faz só uma cópia do
                # dado
                cols[item[0]] = ts.Coluna(item[0], item[1], ft.f_copia)
                qtd_colunas_calculo[item[0]] = 1
            else:
                # usa a função de transformanção informada
                cols[item[0]] = ts.Coluna(item[0], item[1], item[2])

                # terceiro parâmetro é a função de transformação, quarto
                # (se houver) é a quantidade de colunas de entrada que
                # serão usadas no cálculo da coluna de saída
                if len(item) == 3:
                    qtd_colunas_calculo[item[0]] = 1
                else:
                    qtd_colunas_calculo[item[0]] = item[3]

        tab_saida = ts.TabelaSaida(
                nome_tabela_saida, 
                cols, 
                conn_saida)
        if self.__qtd_insercoes_simultaneas is not None:
            tab_saida.qtd_insercoes_simultaneas = self.__qtd_insercoes_simultaneas

        # primeiro limpa tabela de saída, se for o caso
        if estrategia == TpEstrategia.DELETE:
            conn_saida.apaga_registros(nome_tabela_saida)
        elif estrategia == TpEstrategia.TRUNCATE:
            conn_saida.trunca_tabela(nome_tabela_saida)
        elif estrategia == TpEstrategia.INSERT:
            pass
        elif estrategia == TpEstrategia.UPDATE_INSERT:
            pass
        elif estrategia == TpEstrategia.INSERT_UPDATE:
            pass
        elif estrategia == TpEstrategia.UPDATE:
            pass
        else:
            raise NotImplementedError

        qtd_registros = 0
        while True:
            registro = entrada.le_prox_registro()
            if registro is None:
                self.__reset_func_pre_pos_processamento()
                break

            if not self.__funcao_pre_processamento(registro):
                continue

            i = 0
            registro_gravado = []
            for k in cols.keys():
                dados_entrada = []
                for _ in range(qtd_colunas_calculo[k]):
                    dados_entrada.append(registro[i])
                    i += 1

                tab_saida.col[k].calcula_valor( tuple(dados_entrada) )
                registro_gravado.append(tab_saida.col[k].valor)

            if  estrategia == TpEstrategia.UPDATE_INSERT or  \
                estrategia == TpEstrategia.INSERT_UPDATE or  \
                estrategia == TpEstrategia.UPDATE:

                # atualmente, nem todos os métodos de carga implementam essas
                # estratégias
                if cols_chave_update is None:
                    raise NotImplementedError

                if estrategia == TpEstrategia.UPDATE_INSERT:
                    # tenta primeiro atualizar o registro no banco
                    if not tab_saida.atualiza_registro(cols_chave_update):
                        # atualização falhou porque o registro ainda não existia,
                        # então insere-o
                        tab_saida.insere_registro()

                elif estrategia == TpEstrategia.INSERT_UPDATE:
                    # o teste de existência do registro é feito não com base
                    # em chave primária do banco, mas se um registro com exatamente
                    # os mesmos dados na(s) coluna(s) de cols_chave_update já existe
                    # no banco
                    if tab_saida.registro_existe(cols_chave_update):
                        tab_saida.atualiza_registro(cols_chave_update)
                    else:
                        tab_saida.insere_registro()

                elif estrategia == TpEstrategia.UPDATE:
                    tab_saida.atualiza_registro(cols_chave_update)

            else:
                tab_saida.insere_registro()

            qtd_registros += 1
            
            self.__funcao_pos_processamento(registro, tuple(registro_gravado))
 
        if self.__verbose:
            if entrada.nome == "":
                # a consulta de entrada não leu uma só tabela, mas um
                # select provavelmente com joins de tabelas
                print(  str(qtd_registros) +  \
                        " \tregistros lidos dos dados de entrada e" 
                        " salvos na tabela " +  \
                        nome_tabela_saida)
            else:
                print(  str(qtd_registros) +  \
                        " \tregistros de entrada lidos de " + entrada.nome + \
                        " e salvos na tabela " +  \
                        nome_tabela_saida)

    def __monta_dtype(self, cols_saida, usecols, tp_cols_entrada):
        # seta o parâmetro dtype para a importação de planilhas e arquivos csv
        if usecols is None and tp_cols_entrada is None:
            # Todas as colunas do csv ou da planilha foram selecionadas.
            # As colunas de saída terão os mesmos tipos das colunas de entrada.
            dtype = {}
            i = 0
            for item in cols_saida:
                if item[1] == tp.NUMBER:
                    dtype[i] = float
                elif item[1] == tp.INT:
                    dtype[i] = int
                elif item[1] == tp.STRING:
                    dtype[i] = str
                elif item[1] == tp.DATE:
                    dtype[i] = str
                else:
                    raise NotImplementedError

                i += 1
        elif tp_cols_entrada is not None:
            # os tipos das colunas de entrada foram informados explicitamente
            dtype = {}
            i = 0
            for item in tp_cols_entrada:
                if item == tp.NUMBER:
                    dtype[i] = float
                elif item == tp.INT:
                    dtype[i] = int
                elif item == tp.STRING:
                    dtype[i] = str
                elif item == tp.DATE:
                    dtype[i] = str
                else:
                    raise NotImplementedError

                i += 1
        else:
            # pandas vai tentar advinhar os tipos das colunas de entrada
            dtype = None

        return dtype

