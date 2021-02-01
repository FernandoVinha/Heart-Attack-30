from flask import Flask
from data import insert
#from machine_learning import precisao
app = Flask("API")

#metodo da api para verificar a precisão da inteligencia artificial
@app.route("/precision", methods=["GET"])
def precision():
    return {"a precisão é"}
#metodo da api para verificar um novo dado
@app.route("/send", methods=["POST"])
def send():
    body = request.get_json()
    if ("age" not in body):
        return geraResponse(400, "The parameter age is mandatory")
    if ("gender" not in body):
        return geraResponse(400, "The parameter gender is mandatory")
    if ("height" not in body):
        return geraResponse(400, "The parameter height is mandatory")
    if ("weight" not in body):
        return geraResponse(400, "The parameter weight is mandatory")
    if ("ap_hi,ap_lo" not in body):
        return geraResponse(400, "The parameter ap_hi,ap_lo is mandatory")
    if ("cholesterol" not in body):
        return geraResponse(400, "The parameter cholesterol is mandatory")
    if ("gluc" not in body):
        return geraResponse(400, "The parameter gluc is mandatory")
    if ("smoke" not in body):
        return geraResponse(400, "The parameter smoke is mandatory")
    if ("smoke" not in body):
        return geraResponse(400, "The parameter smoke is mandatory")
    if ("alco" not in body):
        return geraResponse(400, "The parameter alco is mandatory")
    if ("active" not in body):
        return geraResponse(400, "The parameter active is mandatory")

        dados_api = insert(body ["age"], body ["gender"], body ["height"], body ["weight"],body ["ap_hi,ap_lo"], body ["cholesterol"], body ["gluc"], body ["smoke"],body ["alco"], body ["active"] )
    return insert
    


def  geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensaguem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response
    
app.run()