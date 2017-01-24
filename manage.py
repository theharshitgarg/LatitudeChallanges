from flask.ext.script import Manager, Server
from mainapp import mainapp

manager = Manager(mainapp)
manager.add_command("runserver", Server(use_debugger=True,
                                        use_reloader=True,
                                        port="8000"))

if __name__=="__main__":
    manager.run()
