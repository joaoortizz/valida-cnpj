from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/")
def read_root():
    return {"status":"error","message":"Try using an ENDPOINT. Example: /validate/[cnpj]"}


@app.get("/validate/{cnpj}")
def read_item(cnpj: str):

    def validate(cnpj):
        import regex
        # defining some variables
        lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
        lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        # cleaning the cnpj
        cnpj = regex.sub('\W','',cnpj)
    
        # finding out the digits
        verificadores = cnpj[-2:]
        
        # verifying the lenght of the cnpj
        if len( cnpj ) != 14: return False
        
        # calculating the first digit
        soma = id = 0
        for numero in cnpj:
            
            # to do not raise indexerrors
            try:
                lista_validacao_um[id]
            except:
                break
                
            soma += int( numero ) * int( lista_validacao_um[id] )
            id += 1
        
        soma = soma % 11
        digito_um = str(0 if soma < 2 else 11 - soma)
        
        # calculating the second digit
        # suming the two lists
        soma = id =0
        
        # suming the two lists
        for numero in cnpj:
            
            # to do not raise indexerrors
            try:
                lista_validacao_dois[id]
            except:
                break
            
            soma += int( numero ) * int( lista_validacao_dois[id] )
            id += 1
        
        # defining the digit
        soma = soma % 11
        digito_dois = str(0 if soma < 2 else 11 - soma)
    
        # returnig
        return bool( verificadores == digito_um + digito_dois )

    def format( cnpj ):
        return "%s.%s.%s/%s-%s" % ( cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14] )
    
    def output(cnpj):
        return {
            "is_valid":validate(cnpj),
            "datetime": datetime.now(),
            "cnpj": format(cnpj)

        }


    return output(cnpj)
