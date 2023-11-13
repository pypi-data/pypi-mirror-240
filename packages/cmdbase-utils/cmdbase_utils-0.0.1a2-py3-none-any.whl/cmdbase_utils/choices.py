from zut import TextChoices, choices_table

app_label = 'cmdbase'

@choices_table(app_label=app_label)
class ReportOrigin(TextChoices):
    API = 'A', "API"
    CODE = 'C'
    ADMIN = 'M'
    WEB = 'W'

@choices_table(app_label=app_label)
class ReportAction(TextChoices):
    CREATE = 'C'
    UPDATE = 'U'
    NOCHANGE = 'N', "No change"
