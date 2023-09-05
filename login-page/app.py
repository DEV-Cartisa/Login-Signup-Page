from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
#debug true, anytime change is made , reruns flask web server 



