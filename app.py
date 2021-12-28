#this is the main programm file
#name: TCHANGMENA A NKEN ALLASSAN
#Date: 27/05/2020
#WedOO.ai first project
#I will make it code challenge
import os , sys
from flask import Flask, request
from pymessenger import Bot,Button
import scenario
import json
import math
import pymongo
from utils import wit_response
from wit import Wit
from twilio.rest import Client
access_token="JFNNF2ZMZNSA2BAT3VVRYVFXSJPNWELC"
client=Wit(access_token)


my_client=pymongo.MongoClient("mongodb+srv://NkenAllassan:tonystarkbot@cluster0-4heam.mongodb.net/<dbname>?retryWrites=true&w=majority")
print('succesfully connected')
db=my_client.get_database('stark')
PAGE_ACCESS_TOKEN="EAAKOFSmCYw4BACC6qtd2rTwjD4WHWSQzbP10DoHg4M8nLvqvGYjgYsNuT1EXCgjFfTxnmZAj2nP9dMIReHwzmlbW0IUXldyc9ZAJlR1687fH3ZAH8Fqr79o1IZBaei5JT5XPhhExfvZCMhI7YvAN18A5PYbj5iK3cUSQQ5uNuMOpw6xsX5LXZB"
people=db.people
account_sid='AC473b63661d3911e1ed1d9a3cfe7c1cb3'
auth_token='b8f346234a6dd9a54a30482d51dfd6bf'
twil_client=Client(account_sid,auth_token)
bot = Bot(PAGE_ACCESS_TOKEN)
symptoms=[]
values=[]
phone=[]
app= Flask(__name__)
@app.route('/',methods=['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"],200
    return "Hello world",200
    #creating my message handler
def message_handler(sender_psid,received_message):
    text=""
    buttons=()
    entity,value=wit_response(received_message)
    if received_message=='bonjour':
        text_1,text_2,text_3,buttons=scenario.ethique()
        return bot.send_text_message(sender_psid,text_1),bot.send_text_message(sender_psid,text_2),bot.send_message(sender_psid,message={"text":text_3,"quick_replies":buttons})
    if entity==['duration']:
        values.append(value[0])
        print(values)
        text,buttons=scenario.fever()
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    else:
        return bot.send_text_message(sender_psid,"veuillez écrire votre age sur ce format: (EX:33ans)")
    if entity==['phone_number']:
        phone.append(value[0])
        return bot.send_text_message(sender_psid,"A présent j'aimerais connaitre votre age (EX:22ans)")
def quick_reply_handler(sender_psid,received_quick_rply):
    buttons=()
    if received_quick_rply["payload"]=="accept":
        text,buttons=scenario.qui()
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="me":
        return bot.send_text_message(sender_psid,"d'accord! à présent j'aimerais avoir votre numéro de télephone.Ceci me permettra de vous contacter si votre état est alarmant")
    if received_quick_rply["payload"]=="other":
        return bot.send_text_message(sender_psid,"ok j'aimerais avoir le nom et numéro de téléphone de celui/celle pour qui vous faite le test")
    if received_quick_rply["payload"]=="reject":
        return bot.send_text_message(sender_psid,"Merci et à la prochaine")
    if received_quick_rply["payload"]=="fever" or received_quick_rply["payload"]=="non fever":
        symptoms.append(received_quick_rply["payload"])
        text,buttons=scenario.cough()
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="toux" or received_quick_rply["payload"]=="non toux":
        symptoms.append(received_quick_rply["payload"])
        text,buttons=scenario.sense()
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="agneusie" or received_quick_rply["payload"]=="anosmie" or received_quick_rply["payload"]=="non odorat":
        text,buttons=scenario.pain()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="douleur a la gorge" or received_quick_rply["payload"]=="courbature" or received_quick_rply["payload"]=="douleur musculaire" or received_quick_rply["payload"]=="douleur a l'abdomen" or received_quick_rply["payload"]=="non abdomen":
        text,buttons=scenario.diarhea()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="diarhea" or received_quick_rply["payload"]=="non diarhea":
        text,buttons=scenario.fatigue()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="repos de +12H" or received_quick_rply["payload"]=="repos de -12H" or received_quick_rply["payload"]=="non fatigue":
        text,buttons=scenario.aliment()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="alimentation difficile" or received_quick_rply["payload"]=="non aliment":
        text,buttons=scenario.souffle()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="manque de souffle" or received_quick_rply["payload"]=="non souffle":
        text,buttons=scenario.heart()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="hypertension" or received_quick_rply["payload"]=="noncardiaque":
        text,buttons=scenario.disease()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="diabetis" or received_quick_rply["payload"]=="cancer" or received_quick_rply["payload"]=="non disease":
        text,buttons=scenario.chronique()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="renale disease" or received_quick_rply["payload"]=="maladie respiratoire" or received_quick_rply["payload"]=="maladie chronique du foie" or received_quick_rply["payload"]=="non chronique":
        text,buttons=scenario.immune()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="baisse de defence immunitaire" or received_quick_rply["payload"]=="immune":
        text,buttons=scenario.sex()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_message(sender_psid,message={"text":text,"quick_replies":buttons},)
    if received_quick_rply["payload"]=="Homme" or received_quick_rply["payload"]=="Femme":
        text,buttons=scenario.save()
        symptoms.append(received_quick_rply["payload"])
        return bot.send_button_message(sender_psid,text,buttons)
    #if buttons_reply["payload"]=="results":
    #    text,resultat=scenario.symptoms_factors(symptoms)
    #    return bot.send_text_message(sender_psid,text +" "+ "taux :"+ str(resultat))

def buttons_handler(sender_psid,buttons_reply):
    buttons=()
    if buttons_reply['payload']=='results':
        text,resultat=scenario.symptoms_factors(symptoms)
        list=scenario.pipeline(symptoms)
        test=scenario.logistique(list,values)
        train=scenario.sigmoide(test)
        if train>= 0.5:
            message=twil_client.messages.create(body='une alerte a été détecter voici les détails:'+text,from_='+12515125105',to='+237698085774')
        a,b=scenario.get_result(train)
        text_1,resultat_1=scenario.facteur_pronostique(symptoms)
        text_2,resultat_2=scenario.facteur_gravite_majeur(symptoms)
        text_3,resultat_3=scenario.facteur_gravite_mineur(symptoms)
        return bot.send_text_message(sender_psid,a),bot.send_text_message(sender_psid,b),bot.send_text_message(sender_psid, 'voici les symptômes associés à votre test: '+ text)
    if buttons_reply['payload']=='save':
        text,resultat=scenario.symptoms_factors(symptoms)
        text_21,buttons=scenario.resultat()
        #list=scenario.pipeline(symptoms)
        #test=scenario.logistique(list,values)
        #train=scenario.sigmoide(test)
        people.update_one({"_id":str(sender_psid)},
        {"$set":{"symptoms":text}},upsert=True)
        #messages=twil_client.messages.create(body='une alerte a été détecter voici les détails:'+text,from_='+12515125105',to='+237698085774')
        #print(messages)
        return bot.send_button_message(sender_psid,text_21,buttons)
        #return bot.send_text_message(sender_psid,"facteurs de gravité majeur:          "+text_2+" "+ "taux :"+ str(resultat_2))
        #return bot.send_text_message(sender_psid,"facteurs de gravité mineur:          "+text_3+" "+ "taux :"+ str(resultat_3))

#postback_handler to handle buttons for the results



@app.route('/',methods=['POST'])
def webhook():
    #symptoms=[]
    data=request.get_json()
    log(data)
    if data["object"]=="page":
        for entry in data["entry"]:
            for message in entry["messaging"]:
                sender_id=message["sender"]["id"]
                recipient_id=message["recipient"]["id"]
                if message.get("message"):
                    if 'quick_reply' in message["message"]:
                        message_qck_reply=message["message"]["quick_reply"]
                        #symptoms.append(message_qck_reply['payload'])
                        quick_reply_handler(sender_id,message_qck_reply)
                    #elif "attachments" in message['message']:
                    #    buttons_reply=message["message"]["attachments"][0]["payload"]['buttons']
                    #    buttons_handler(sender_id,buttons_reply)
                    elif "text" in message["message"]:
                        message_text=message["message"]["text"]
                        #entity,value=wit_response(message_text)
                        message_handler(sender_id,message_text)
                    else:
                        bot.send_text_message(sender_id,'veuiller dire un bonjour à notre bot')
            if "postback" in entry["messaging"][0]:
                buttons_reply=entry["messaging"][0]["postback"]
                buttons_handler(sender_id,buttons_reply)
                log('stark')
            else:
                buttons_reply= None

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__=="__main__":
    app.run(debug=True,port=80)
