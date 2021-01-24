from src.command.test_cmd import TestCMD
from src.command.votekick_zajma import VotekickZajma
from src.command.bajo_jajo import bajo_jajo
from src.command.help import print_help
from src.command.votekick import Votekick
from src.command.run_code import run_code

test_cmd = TestCMD()
votekick_zajma = VotekickZajma()
votekick = Votekick()

context_free_command_db = {
    '+test': lambda args: test_cmd.run(),
    '+votekick zajma': lambda args: votekick_zajma.run(),
    '+bajo jajo': lambda args: bajo_jajo(),
    '+help': lambda args: print_help(),
    '+votekick stats': lambda args: votekick.stats()
}

start_with_command_db = {
    '+votekick': lambda args: votekick.run(args),
    '+run': lambda args: run_code(args)
}