import threading
from github import Github

pain = 0

def printit():
  threading.Timer(30, printit).start()
  global pain
  pain = pain + 1

  g = Github("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")
  repo = g.get_repo("msubb/parking")
  contents = repo.get_contents("index.html", )
  repo.update_file(contents.path, "test 1", """<!DOCTYPE html>
  <html>
    <head>
      <title>Testing</title>

      <style>

      #Blue {
        background-color: rgb(31, 31, 202);
  	  color: white;
        height: auto;
        position: static;
        top: 0;
        left: 0;
        width: 100%;
      }

  	#Red {
        background-color: rgb(202, 31, 31);
  	  color: white;
        height: auto;
        position: static;
        top: 0;
        left: 0;
        width: 100%;
      }

      body{
        background: grey;
        margin: 0;
      }

      </style>

    </head>

    <body>

  <section id="Blue">
  	<h1 style="font-size:4em; ">
  		<center>""" + str(pain) + """</center>
  	</h1>
  </section>

  <section id="Red">
  	<center>Testingss</center>
  </section>

    </body>
  </html>""", contents.sha)

  print(pain)


printit()