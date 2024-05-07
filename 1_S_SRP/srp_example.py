# class Process:
#     def handle(self, username: str, password: str) -> None:
#         if isinstance(username, str) and isinstance(password, str):
#             print('Acessando o banco de dados...')
#             print('Verificando existencia do usuario...')
#             print('Cadastro de usuários realizado com sucesso!')
#         else:
#             raise Exception('Dados Invalidos')

class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error('Dados Invalidos')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando existencia do usuario...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuários realizado com sucesso!')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)


# “Um módulo deve ter um, e apenas um, motivo para alteração”

