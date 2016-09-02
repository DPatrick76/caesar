import webapp2
from caesar import encrypt
import cgi

form="""
        <html>
    <head>
        <style>
            form {
                background-color:#ccff99;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(value)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self, value=""):
        self.response.out.write(form % {"value":value})

    def get(self):
        self.write_form()

    def post(self):
        userNumber = self.request.get('rot')
        userNumber = int(userNumber)
        userText = self.request.get("text")
        userText = cgi.escape(userText, quote=True)
        userText = encrypt(userText,userNumber)
        #userText = cgi.escape(userText, quote=True)
        self.write_form(userText)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
