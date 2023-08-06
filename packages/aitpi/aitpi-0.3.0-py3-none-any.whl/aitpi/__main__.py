import aitpi
from aitpi.printer import Printer
from aitpi import router

class Watcher():
    def consume(self, message):
        Printer.print(" Watcher: %s %s" % (message.name, message.event))
        if (message.name == "command0" and message.event == "1"):
            aitpi.changeInputRegLink("Button0", "command1")
        elif (message.name == "command1" and message.event == "1"):
            aitpi.changeInputRegLink("Button0", "command0")

        print(message.attributes)

router.addConsumer([1], Watcher())

aitpi.addRegistry("../example_command_registry.json", "../example_foldered_commands.json")
aitpi.addRegistry("../reg2.json")

aitpi.initInput("../example_input.json")


print(aitpi.getFolderedCommands("../example_foldered_commands.json", "Presets"))

print("COMMANDS: ", aitpi.getCommands())

while (True):
    input()