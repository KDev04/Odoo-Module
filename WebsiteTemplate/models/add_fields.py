from odoo import _, models, fields, api
from datetime import datetime


class ProductTable(models.Model):
    _name = "product_table_block_description"
    product_table_block_id = fields.Many2one(
        "product.template", string="Product FK block title ID"
    )
    # sl_no = fields.Integer(string="No.")
    product_table_block_title = fields.Char(string="Title")
    product_table_block_description = fields.Text(string="Description")
    product_table_block_image = fields.Image(string="Image")
    product_table_block_type = fields.Selection(
        [
            ("image_right", "Image Right"),  # Lựa chọn 1: Image Right
            ("image_left", "Image Left"),  # Lựa chọn 2: Image Left
            ("picture", "Picture"),  # Lựa chọn 3: Banner
            ("gallery", "Gallery"),
        ],
        string="Block Type",
        default="image_right",
    )
    sequence = fields.Integer(string="Sequence", index=True)


class ProductTableView(models.Model):
    _inherit = "product.template"
    product_template_id = fields.One2many(
        "product_table_block_description",
        "product_table_block_id",
        string="Product Block ID",
    )

    # checkAddBanner = fields.Boolean(string="Add banner")

    # @api.model
    # def create(self, vals):
    #     # Tạo một đối tượng mới của product.template
    #     product_template = super(ProductTableView, self).create(vals)
    #     # Lấy danh sách các dòng trong product_template
    #     lines = product_template.product_template_id
    #     # Thiết lập giá trị cho trường sl_no của từng dòng
    #     for index, line in enumerate(lines, start=1):
    #         line.sl_no = index
    #     return product_template

    # @api.onchange('product_template_id')
    # def _onchange_product_template_id(self):
    #     # Tính toán và gán lại giá trị cho trường sl_no khi có sự thay đổi trong product_template_id
    #     for index, line in enumerate(self.product_template_id, start=1):
    #         line.sl_no = index

    checkAddDetail = fields.Boolean(string="Description Blocks")
    titleArr = fields.Text()
    descriptionArr = fields.Text()
    imageArr = fields.Binary()

    @api.model
    def create(self, values):
        if "checkAddDetail" in values:
            values["checkAddDetail"] = values.pop("checkAddDetail")
        return super(ProductTableView, self).create(values)

    def write(self, values):
        if "checkAddDetail" in values:
            values["checkAddDetail"] = values.pop("checkAddDetail")
        return super(ProductTableView, self).write(values)
