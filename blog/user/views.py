from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSignupSerializer, UserLoginSerialzer

from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup_view(request):
    serializer = UserSignupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors)
    
@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerialzer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({
            "message" : "로그인 성공"
        }, status=status.HTTP_200_OK)

        response["Authorization"] = f"Bearer {access_token}"

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite='Lax',
            secure=False
        )

        return response
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permission_view(request):
    return Response({
        "message": f"{request.user.username}님, 인증된 사용자입니다."
    })