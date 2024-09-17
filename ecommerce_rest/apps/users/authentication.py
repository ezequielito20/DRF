from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    def expires_in(self,token):
        # return left time of token
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self,token):
        # return True if token is alive or False if token is expired
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self,token):
        """
    Return:
        * is_expire     : True if token is alive, False if token is expired
        * token         : New token or actual token
    """
    is_expire = self.is_token_expired(token)
    if is_expire:
        user = token.user
        token.delete()
        token = self.get_model().objects.create(user=user)
    
    return toke

    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)

        except : 
            self.get_model().DoesNotExist
            raise AuthenticationFailed('token invalido')
        
        if not token.user.is_active:
            raise AuthenticationFailed('user inactive or deleted')

        is_expired = self.token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed('Su token ha expirado')
        
        return (token.user, token)