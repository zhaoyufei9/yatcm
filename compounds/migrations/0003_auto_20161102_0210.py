# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 02:10
from __future__ import unicode_literals

import compounds.models
from django.db import migrations, models
import django.db.models.deletion
import django_rdkit.models.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0002_auto_20161102_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='KEGGCompound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegg_id', models.CharField(max_length=64, verbose_name='KEGG ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('mol', django_rdkit.models.fields.MolField(blank=True, null=True, verbose_name='An RDKit molecule')),
                ('mol_block', models.TextField(blank=True, null=True, verbose_name='Mol block')),
                ('smiles', models.TextField(blank=True, max_length=1024, null=True)),
                ('mol_image', models.ImageField(blank=True, null=True, storage=compounds.models.OverwirteStorage, upload_to='mol_image/')),
            ],
        ),
        migrations.CreateModel(
            name='KEGGPathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegg_id', models.CharField(max_length=64, verbose_name='KEGG ID')),
                ('name', models.CharField(max_length=128)),
                ('kgml', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, storage=compounds.models.OverwirteStorage, upload_to='kegg_pathway_image/')),
            ],
        ),
        migrations.CreateModel(
            name='KEGGPathwayCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='compounds.KEGGPathwayCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KEGGSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(blank=True, null=True)),
                ('kegg_compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.KEGGCompound')),
                ('tcm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.Compound')),
            ],
        ),
        migrations.AddField(
            model_name='keggpathway',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.KEGGPathwayCategory'),
        ),
        migrations.AddField(
            model_name='keggcompound',
            name='pathway',
            field=models.ManyToManyField(to='compounds.KEGGPathway'),
        ),
        migrations.AddField(
            model_name='keggcompound',
            name='similar_to_tcm',
            field=models.ManyToManyField(through='compounds.KEGGSimilarity', to='compounds.Compound'),
        ),
    ]