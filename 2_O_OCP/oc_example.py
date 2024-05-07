# class Company:
#     def do_work(self, worker: int) -> None:
#         if worker == 1:
#             print('Programmer creating code')
#         elif worker == 2:
#             print('Seller selling the product')
#         elif worker == 3:
#             print('Human Resources hiring new devs')
#         else:
#             print('Error, no Worker')

class Programmer:
    def make(self):
        print('Programmer creating code')


class Seller:
    def make(self):
        print('Seller selling the product')


class RH:
    def make(self):
        print('HR hiring new devs')


class Company:
    def do_work(self, worker: any) -> None:
        worker.make()


programmer = Programmer()
seller = Seller()
rh = RH()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)

# "Um artefato de software deve estar aberto para extensão, mas fechado para modificação"
