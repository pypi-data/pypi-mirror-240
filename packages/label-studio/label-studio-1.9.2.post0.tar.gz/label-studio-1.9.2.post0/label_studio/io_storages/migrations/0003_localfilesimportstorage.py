# Generated by Django 3.1.4 on 2021-03-18 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210314_1840'),
        ('tasks', '0005_auto_20210309_1239'),
        ('io_storages', '0002_auto_20210311_0530'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalFilesMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(blank=True, help_text='Local path', null=True, verbose_name='path')),
                ('regex_filter', models.TextField(blank=True, help_text='Regex for filtering objects', null=True, verbose_name='regex_filter')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
            ],
        ),
        migrations.CreateModel(
            name='LocalFilesExportStorage',
            fields=[
                ('localfilesmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.localfilesmixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('last_sync', models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync')),
                ('last_sync_count', models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_localfilesexportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.localfilesmixin', models.Model),
        ),
        migrations.CreateModel(
            name='LocalFilesImportStorage',
            fields=[
                ('localfilesmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.localfilesmixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('last_sync', models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync')),
                ('last_sync_count', models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_localfilesimportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.localfilesmixin', models.Model),
        ),
        migrations.CreateModel(
            name='LocalFilesImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_localfilesimportstoragelink', to='tasks.task')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.localfilesimportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalFilesExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_localfilesexportstoragelink', to='tasks.annotation')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.localfilesexportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
