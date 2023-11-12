from typing import Optional

from pydantic import BaseModel, Field


class user_data(BaseModel):
    user_id: str = Field(title='user_id', example='zisu17')


class login_data(user_data):
    user_nm: str = Field(title='이름', example='홍길동')
    user_birth: str = Field(title='생년월일', example='19990802')
    user_phone1: str = Field(title='식별번호 (010", "011", "016", "017", "018", "019")', example='010')
    user_phone2: str = Field(title='휴대폰번호 (앞의 3자리를 제외한 번호)', example='11112222')
    telecom: str = Field(None, title='통신사 ("SKT", "KT", "LGU+")', example='KT')

class make_user_data(user_data):
    user_nm: str = Field(title='이름', example='홍길동')
    rsdntrgnmb1: str = Field(title='주민등록번호 앞자리', example='990802')
    rsdntrgnmb2: str = Field(title='주민등록번호 뒷자리', example='1234567')
    user_phone1: str = Field(title='식별번호 (010", "011", "016", "017", "018", "019")', example='010')
    user_phone2: str = Field(title='휴대폰번호 (앞의 3자리를 제외한 번호)', example='11112222')
    telecom: str = Field(None, title='통신사 ("SKT", "KT", "LGU+")', example='KT')


class update_user_data(user_data):
    user_nm: Optional[str] = Field(title='이름', example='홍길동')
    user_phone1: Optional[str] = Field(title='식별번호 (010", "011", "016", "017", "018", "019")', example='010')
    user_phone2: Optional[str] = Field(title='휴대폰번호 (앞의 3자리를 제외한 번호)', example='11112222')
    telecom: Optional[str] = Field(title='통신사 ("SKT", "KT", "LGU+")', example='KT')

