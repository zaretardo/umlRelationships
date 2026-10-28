# Dependency: ReportGenerator temporarily uses Printer

class Printer:
    def print_report(self, report):
        print(f"Printing report: {report}")


class ReportGenerator:
    def generate_report(self, printer):
        report = "School Activity Report"
        printer.print_report(report)


printer = Printer()
generator = ReportGenerator()

generator.generate_report(printer)