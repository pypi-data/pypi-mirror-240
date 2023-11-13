import os
from typing import List, Tuple

from dftools.events import DfLoggable, StandardExtendedInfoEvent, StandardErrorEvent
from dftools.exceptions import MissingMandatoryArgumentException, NoFileAtLocation
from dftools.core.structure import Namespace
from dftools.core.database.query_result import QueryExecResult, QueryExecResults


class ConnectionWrapper(DfLoggable):
    """
        Connection Wrapper interface
        All connection wrappers should implement this interface
    
        Connection Wrapper should maintain the local variables :
            - Session variables 
                - Session ID (session_id)
    """
    def __init__(self) -> None:
        super().__init__()
        self.session_id = None

    # Connection methods
    def get_current_catalog(self) -> str:
        """
        Returns the currently active catalog for this connection.
        
        Returns
        -----------
            catalog_name : str
                The catalog name
        """
        return NotImplementedError('The get_current_catalog method is not implemented')

    def get_current_namespace_name(self) -> str:
        """
        Returns the currently active namespace name (also named schema name) for this connection.
        
        Returns
        -----------
            namespace_name : str
                The namespace name
        """
        return NotImplementedError('The get_current_namespacename method is not implemented')

    def get_current_namespace(self) -> Namespace:
        """
        Returns the currently active namespace (also named schema) for this connection.
        
        Returns
        -----------
            namespace : Namespace
                The namespace
        """
        return NotImplementedError('The get_current_namespace method is not implemented')
    
    def close_connection(self):
        """
        Closes the connection currently stored in this wrapper

        Returns
        -----------
            close_status : str
                The connection close status
        """
        return NotImplementedError('The close_connection method is not implemented')

    # Query and script execution methods

    def execute_script(self, file_path : str, delimiter : str = ';') -> QueryExecResults:
        """
        Executes a script on this connection wrapper

        Parameters
        -----------
            file_path : str
                The file path of the script to execute
            delimiter : str
                The statements' delimiter (defaulted to ";")
        
        Returns
        -----------
            The queries exec results
        """
        if file_path is None :
            raise MissingMandatoryArgumentException(method_name='Execute Script', object_type=type(self), argument_name='File Path')
        if not os.path.exists(file_path):
            raise NoFileAtLocation(file_path=file_path)
        with open(file_path, 'r') as file :
            file_data = file.read()
        queries = file_data.split(delimiter)
        queries = [query.rstrip().lstrip() for query in queries if len(query.rstrip().lstrip()) > 0]
        self.log_event(StandardExtendedInfoEvent('Execution of SQL file : ' + os.path.basename(file_path) + ' - Start'))
        query_exec_result_list = self.execute_queries([(query, None) for query in queries])
        self.log_event(StandardExtendedInfoEvent('Execution of SQL file : ' + os.path.basename(file_path) + ' - Successful'))
        return query_exec_result_list

    def execute_scripts(self, file_path_list : List[str], delimiter : str = ';') -> List[Tuple[str, QueryExecResults]]:
        """
        Executes scripts on this connection wrapper

        Parameters
        -----------
            file_path_list : List[str]
                The list of file paths of the script to execute
            delimiter : str
                The statements' delimiter (defaulted to ";")
        
        Returns
        -----------
            A list of tuples containing the absolute path of the script executed and the queries exec results
        """
        query_exec_result_list = []
        for file_path in file_path_list :
            try :
                query_exec_result_list.append((os.path.abspath(file_path), self.execute_script(file_path, delimiter)))
            except Exception as e:
                self.log_event(StandardErrorEvent(e.msg))
        return query_exec_result_list
    
    def execute_query(self, query : str, name : str = '') -> QueryExecResult:
        """
        Executes a query on the connection contained in the wrapper.
        An error should be raised according to the specificities of each database

        Parameters
        -----------
            query : str
                The query to execute
            name : str, Optional
                The name of the query to execute, for informational purposes
        
        Returns
        -----------
            result_set_list : The list of result set, or None if query encountered an error
        """
        return NotImplementedError('The execute_query method is not implemented')
    
    def execute_queries(self, query_list : List[Tuple[str, str]], stop_on_error : bool = True) -> QueryExecResults:
        """
        Executes a list of queries on the snowflake connection contained in the wrapper.
        An error should be raised according to the specificities of each database

        Local Variables are set to the query before the execution. 
        Available variables are :
            - session_id : the current session id
            - last_query_exec_result : the last query execution result; from the previous query execution inside this method
                , thus the first query is provided an empty last_query_exec_result

        Parameters
        -----------
            query_list : List[Tuple[str, str]]
                The list of queries to execute with the name of the query
            stop_on_error : boolean
                Flag which stops the execution on the first execution error when true
        
        Returns
        -----------
            The queries exec results
        """
        query_exec_results = QueryExecResults()
        last_query_exec_result = None
        for query_tuple in query_list:
            original_query = query_tuple[0]
            query_name = query_tuple[1] if len(query_tuple) > 1 else None
            query = original_query.format(session_id = self.session_id, last_query_exec_result = last_query_exec_result)
            query_exec_result = self.execute_query(query, query_name)
            query_exec_results.append(query_exec_result)
            last_query_exec_result = query_exec_result
            if query_exec_result.is_error() & stop_on_error:
                break
        return query_exec_results