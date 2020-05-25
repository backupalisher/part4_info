# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthAssignment(models.Model):
    item_name = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_assignment'


class AuthItem(models.Model):
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    rule_name = models.CharField(max_length=64, blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_item'


class AuthItemChild(models.Model):
    parent = models.CharField(max_length=64)
    child = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'auth_item_child'


class AuthRule(models.Model):
    name = models.CharField(max_length=64)
    data = models.BinaryField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_rule'


class Brands(models.Model):
    name = models.CharField('Бренд', help_text='Наименование производителя', max_length=255)
    logotype = models.ImageField('Логотип', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'brands'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Cartridge(models.Model):
    brand_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartridge'


class CartridgeAnalogModel(models.Model):
    brand_id = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartridge_analog_model'


class Categories(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class DetailOptions(models.Model):
    caption_spr_id = models.SmallIntegerField()
    detail_option_spr_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_options'


class DetailStatistics(models.Model):
    detail_id = models.BigIntegerField()
    count_click = models.IntegerField()
    count_view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detail_statistics'


class Details(models.Model):
    partcode_id = models.IntegerField(blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    module_id = models.SmallIntegerField(blank=True, null=True)
    spr_detail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'


class ErrorCode(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    display = models.TextField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    description_id = models.IntegerField(blank=True, null=True)
    causes_id = models.IntegerField(blank=True, null=True)
    remedy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_code'


class Favorites(models.Model):
    user_id = models.IntegerField()
    detail_id = models.BigIntegerField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'favorites'


class FilterSettings(models.Model):
    caption = models.CharField(max_length=255, blank=True, null=True)
    subcaption = models.CharField(max_length=255, blank=True, null=True)
    sub_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    values = models.TextField(blank=True, null=True)  # This field type is a guess.
    caption_en = models.CharField(max_length=255, blank=True, null=True)
    subcaption_en = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_settings'


class LinkCartdgeAnalog(models.Model):
    # cartridge_id = models.IntegerField(blank=True, null=True)
    # cartridge_analog_id = models.IntegerField(blank=True, null=True)
    cartridge_id = models.ForeignKey(Cartridge, on_delete=models.SET_NULL, null=True)
    cartridge_analog_id = models.ForeignKey(CartridgeAnalogModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False
        db_table = 'link_cartdge_analog'


class LinkCartridgeModelAnalog(models.Model):
    cartridge_id = models.IntegerField(blank=True, null=True)
    cartrindge_analog_model_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_cartridge_model_analog'


class LinkCartridgeOptions(models.Model):
    cartridge_id = models.IntegerField(blank=True, null=True)
    spr_cartridge_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_cartridge_options'


class LinkDetailsOptions(models.Model):
    detail_id = models.BigIntegerField()
    detail_option_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_details_options'


class LinkModelErrorCode(models.Model):
    model_id = models.IntegerField()
    error_code_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_model_error_code'


class LinkModelModuleImage(models.Model):
    model_id = models.IntegerField()
    spr_module_id = models.IntegerField(blank=True, null=True)
    spr_module_image_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_model_module_image'


class LinkPartcodeModelAnalogs(models.Model):
    model_id = models.IntegerField(blank=True, null=True)
    partcode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_partcode_model_analogs'


class Market(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    partcode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market'


class Media(models.Model):
    link = models.CharField(max_length=500)
    alt = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    saller_id = models.IntegerField()
    detail_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'media'


class Migration(models.Model):
    version = models.CharField(max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


class Models(models.Model):
    name = models.CharField(max_length=255)
    brand_id = models.IntegerField(blank=True, null=True)
    main_image = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'models'


class OrderDetails(models.Model):
    saller_id = models.IntegerField()
    detail_id = models.BigIntegerField()
    order_id = models.IntegerField()
    tatal_count = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_details'


class Orders(models.Model):
    fio = models.CharField(max_length=255)
    address = models.CharField(max_length=1500, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    ordered_date = models.DateField(blank=True, null=True)
    paid = models.BooleanField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class PagesSeo(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=5000, blank=True, null=True)
    keywords = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_seo'


class Partcodes(models.Model):
    code = models.TextField()
    description = models.TextField(blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partcodes'


class PayHistory(models.Model):
    user_id = models.IntegerField()
    date_pay = models.DateField()
    discription = models.CharField(max_length=500, blank=True, null=True)
    order_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pay_history'


class Profile(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    public_email = models.CharField(max_length=255, blank=True, null=True)
    gravatar_email = models.CharField(max_length=255, blank=True, null=True)
    gravatar_id = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=40, blank=True, null=True)
    type_pay = models.CharField(max_length=45, blank=True, null=True)
    subscriber = models.BooleanField()
    address = models.CharField(max_length=1500, blank=True, null=True)
    pro_status = models.BooleanField()
    avatar = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'


class SellerHasDetails(models.Model):
    detail_id = models.BigIntegerField()
    saller_id = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_count = models.SmallIntegerField()
    condition = models.CharField(max_length=50, blank=True, null=True)
    warranty = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_has_details'


class SellerOffices(models.Model):
    saller_id = models.IntegerField()
    address = models.CharField(max_length=1500, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    worktime = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_offices'


class Sellers(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    guarantee = models.CharField(max_length=1500, blank=True, null=True)
    nds = models.SmallIntegerField(blank=True, null=True)
    delivery = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers'


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'services'


class SocialAccount(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_account'


class SprCartridgeOptions(models.Model):
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_cartridge_options'


class SprDetailOptions(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_detail_options'


class SprDetails(models.Model):
    name = models.TextField(blank=True, null=True)
    name_ru = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    seo = models.TextField(blank=True, null=True)
    base_img = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_details'


class SprErrorCode(models.Model):
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_error_code'


class SprErrorCodeImage(models.Model):
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_error_code_image'


class SprModuleImage(models.Model):
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_module_image'


class SprModules(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1500, blank=True, null=True)
    scheme_picture = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_modules'
