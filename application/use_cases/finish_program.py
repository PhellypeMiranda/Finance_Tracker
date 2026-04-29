from application.exceptions.exit_program import ExitProgram

class FinishProgramUseCase:
    @staticmethod
    def execute():
        raise ExitProgram()