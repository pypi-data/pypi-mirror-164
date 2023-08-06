import jwt

from .serializers import PaymentSerializer, CancelOrderSerializer


class Talar:
    """
    Talar integration class. Used to perform actions for Talar API.
    """

    def __init__(self, project_id, key_id, key_secret,
                 base_url="https://secure.talar.app"):
        self.project_id = project_id

        self.key_id = key_id
        self.key_secret = key_secret

        self.base_url = base_url

    @property
    def url(self):
        return f'{self.base_url}/project/{self.project_id}/payment/create/'

    @property
    def cancel_order_url(self):
        return f'{self.base_url}/project/{self.project_id}/payment/cancel/'

    def _handle_payment_data(self, serializer, data: dict):
        talar_serializer = serializer(data=data)
        talar_serializer.is_valid(raise_exception=True)

        encrypted_data = jwt.encode(
            talar_serializer.data,
            self.key_secret,
            algorithm='HS256',
            headers={'kid': self.key_id}
        )
        return encrypted_data.decode("utf-8")

    def create_payment_data(self, data: dict):
        return self._handle_payment_data(PaymentSerializer, data)

    def cancel_payment_data(self, data: dict):
        return self._handle_payment_data(CancelOrderSerializer, data)
