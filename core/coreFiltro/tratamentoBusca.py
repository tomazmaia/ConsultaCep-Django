
class TratamentoBusca:
    cep = {}

    def tratQuantidadeENumeral(self,cep):
        self.cep = cep
        if cep.isnumeric and len(self.cep) == 8:
            return True
        return False


