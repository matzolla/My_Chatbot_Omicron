from flask import Flask, request



app=Flask(__name__)
@app.route('/',methods=[GET])
def verify():
    # webhook verification
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"],200
    return "Hello world",200
## ligne de code ici


@app.route('/',methods=[POST])

## ligne de code ici


if __name__=='main':
    app.run(debug=True,port=80)
