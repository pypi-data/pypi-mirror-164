# Generated by Django 3.2.5 on 2021-09-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ref",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "authors",
                    models.TextField(
                        blank=True,
                        help_text='Comma-delimited names with space-separated initials first (no ANDs). e.g. "A. N. Other, B.-C. Person Jr., Ch. Someone-Someone, N. M. L. Haw Haw"',
                    ),
                ),
                (
                    "title",
                    models.TextField(
                        blank=True,
                        help_text="Best-effort UTF-8 encoded plaintext version of title. No HTML tags, markdown or LaTeX.",
                    ),
                ),
                (
                    "title_html",
                    models.TextField(
                        blank=True,
                        help_text="Valid HTML version of title. Don't wrap with &lt;p&gt; or other tags.",
                    ),
                ),
                (
                    "title_latex",
                    models.TextField(
                        blank=True,
                        help_text="LaTeX version of title. Don't escape backslashes (\\) but do use valid LaTeX for accented and similar characers.",
                    ),
                ),
                ("journal", models.CharField(blank=True, max_length=500)),
                ("volume", models.CharField(blank=True, max_length=10)),
                ("page_start", models.CharField(blank=True, max_length=10)),
                ("page_end", models.CharField(blank=True, max_length=10)),
                ("article_number", models.CharField(blank=True, max_length=16)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("note", models.TextField(blank=True)),
                ("note_html", models.TextField(blank=True)),
                ("note_latex", models.TextField(blank=True)),
                ("doi", models.CharField(blank=True, max_length=100)),
                ("bibcode", models.CharField(blank=True, max_length=19)),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        help_text="If not provided, this will be automatically constructed as https://dx.doi.org/&lt;DOI&gt; if possible.",
                    ),
                ),
                ("bibtex", models.TextField(blank=True, null=True)),
                ("ris", models.TextField(blank=True, null=True)),
                ("citeproc_json", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
