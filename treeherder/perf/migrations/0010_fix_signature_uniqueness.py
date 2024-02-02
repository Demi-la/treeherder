# Generated by Django 1.11.15 on 2018-09-28 11:41
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('model', '0010_remove_runnable_job'),
        ('perf', '0009_non_nullable_issue_tracker'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='performancesignature',
            unique_together=set(
                [
                    (
                        'repository',
                        'framework',
                        'platform',
                        'option_collection',
                        'suite',
                        'test',
                        'last_updated',
                        'extra_options',
                    ),
                    ('repository', 'framework', 'signature_hash'),
                ]
            ),
        ),
    ]
