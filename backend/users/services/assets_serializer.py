from marshmallow import Schema, fields, validate

# Serializer for the Stock model
class StockSchema(Schema):
    id = fields.String(dump_only=True)
    symbol = fields.String(required=True, validate=validate.Length(max=10))
    company_name = fields.String(required=True, validate=validate.Length(max=255))
    quantity = fields.Float(validate=validate.Range(min=0))
    price = fields.Float(validate=validate.Range(min=0))

# Serializer for the Bond model
class BondSchema(Schema):
    issuer = fields.Str(required=True)
    face_value = fields.Float(required=True, validate=validate.Range(min=0))
    yield_rate = fields.Float(required=True, validate=validate.Range(min=0))
    maturity_date = fields.Date(required=True)

class CashAccountSchema(Schema):
    id = fields.String(dump_only=True)  # Field is read-only (dump-only)
    account_name = fields.String(required=True, validate=validate.Length(max=255))
    account_type = fields.String(validate=validate.Length(max=100))
    balance = fields.Float(required=True, validate=validate.Range(min=0))
    currency = fields.String(required=True, validate=validate.Length(max=10))

class CryptocurrencySchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=255))
    symbol = fields.String(required=True, validate=validate.Length(max=10))
    quantity = fields.Float(validate=validate.Range(min=0))
    price = fields.Float(validate=validate.Range(min=0))

class ETFSchema(Schema):
    id = fields.String(dump_only=True)
    symbol = fields.String(required=True, validate=validate.Length(max=10))
    fund_name = fields.String(required=True, validate=validate.Length(max=255))
    price = fields.Float(validate=validate.Range(min=0))

class FundSchema(Schema):
    id = fields.String(dump_only=True)
    fund_name = fields.String(required=True, validate=validate.Length(max=255))
    symbol = fields.String(required=True, validate=validate.Length(max=10))
    nav = fields.Float(validate=validate.Range(min=0))
    fund_type = fields.String(required=True, validate=validate.Length(max=50))

class OptionsDerivativesSchema(Schema):
    id = fields.String(dump_only=True)
    contract_name = fields.String(required=True, validate=validate.Length(max=255))
    underlying_asset = fields.String(validate=validate.Length(max=255))
    contract_type = fields.String(validate=validate.Length(max=100))
    expiration_date = fields.Date()
    price = fields.Float()

class PortfolioSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, max_length=255)
    user_id = fields.String(required=True)

class PrivateEquitySchema(Schema):
    id = fields.String(dump_only=True)
    fund_name = fields.String(required=True, validate=validate.Length(max=255))
    commitment_amount = fields.Float(validate=validate.Range(min=0))
    current_value = fields.Float(validate=validate.Range(min=0))

class RealEstateSchema(Schema):
    id = fields.String(dump_only=True)
    property_name = fields.String(required=True, validate=validate.Length(max=255))
    property_type = fields.String(validate=validate.Length(max=100))
    value = fields.Float(validate=validate.Range(min=0))
    location = fields.String(validate=validate.Length(max=255))

class REITSchema(Schema):
    id = fields.String(dump_only=True)
    property_name = fields.String(required=True, validate=validate.Length(max=255))
    symbol = fields.String(required=True, validate=validate.Length(max=10))
    price_per_share = fields.Float(validate=validate.Range(min=0))

class UsersSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=255))
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.String(required=True, validate=validate.Length(min=8))
