log_format = "<b><green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green></b><b><level> [{level: ^2}]: </level></b><b><i>{message}</i></b>"

Start = '<red>{"Thread Num": "%s", "Retry": "%s", "Pid": "%s", "Download_Delay": "%s", "Download_Num": "%s", "LOG_LEVEL": "%s"}</red>'


def close_sign(data):
    column_widths = max(len(header) for header, _ in data) + 7
    m = f"<red>\n"
    m += f"| {'Key':<{column_widths}} | {'Value':<{column_widths}} |\n"
    m += "| " + "-" * (column_widths + 1) + "| " + "-" * (column_widths + 1) + "|\n"
    for header, value in data:
        m += f"| `{header}`{' ' * (column_widths - len(header) - 2)} | `{value}`{' ' * (column_widths - len(str(value)) - 2)} |\n"
    m += "</red>"
    return m
