from bookreview import create_app
#from OpenSSL import SSL
#import ssl

#context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.load_cert_chain('cert.pem','key.pem')
#context=SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_certificate('cert.pem')
#context.use_privatekey('key.pem')

app = create_app()

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0',ssl_context=context)
    app.run(host='0.0.0.0',ssl_context=('cert.pem','key.pem'))
