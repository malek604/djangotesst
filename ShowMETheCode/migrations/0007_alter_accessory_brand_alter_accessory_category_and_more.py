# Generated by Django 4.2.7 on 2023-12-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowMETheCode', '0006_brand_category_color_material_alter_accessory_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='brand',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='ShowMETheCode.brand'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='ShowMETheCode.category'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='color',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='ShowMETheCode.color'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='material',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='ShowMETheCode.material'),
        ),
    ]
