from django.db import models


class OptionFields(models.Model):
    a = models.CharField(null=True,blank=True,choices="",db_column="")
    # null
    # 기본값 False, True를 사용하는건 추천하지 않는다
    # 대부분의 <no data>에 대해 중복된 값으로 처리한다
    a = model.CharField(null=Ture)

    # blank
    # 기본값 False, True시에도 null 이지만 유효성 검사에 달라진다
    # 유효성 검사시 빈 값('')을 받는다
    a = model.CharField(blank=True)

    # choices
    # 라디오 버튼을 생각하면 된다
    # 이곳에서는 하위 클래스로 간결하게 정의 가능한것을 가져왔다
    # 참조 : [choice](https://docs.djangoproject.com/ko/3.1/ref/models/fields/#choices)
    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')

    year_in_school = models.CharField(
    max_length=2,
    choices=YearInSchool.choices,
    default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

    # db_colum
    # 이 필드에 사용할 데이터베이스의 열의 이름
    # 이게 주어지지 않으면 Django는 필드의 이름을 사용한다
    a = model.CharField(db_colum="name")

    # db_index
    # True인 경우에 필드에 대한 데이터베이스 색인이 생성된다
    # 색인은 검색 속도를 높이기 위해 쓰는 작업
    a = model.CharField(db_index=True)

    # db_tablespace
    # 이 필드가 인덱싱 된 경우에, 필드의 인덱스에 사용할 데이터베이스 테이블 스페이스의 이름
    # settings.py에  DEFAULT_INDEX_TABLESPACE 를 설정 해줘야 한다, 기본값은 '' 빈값이다
    # 지원하지 않는다면 무시된다
    a = models.CharField(db_tablespace='')

    # default
    # 필드의 기본값을 지정한다, 이것은 값 또는 호출 가능한 객체 일 수 있습니다
    # 호출 가능하면 새 객체가 생성 될 때마다 호출된다
    # 그러니까 함수가 사용이 가능하다... 아주좋네
    # 기본값은 변경 가능한 객체는 불가능하다
    # 다음은 Docs의 예시이다
    def contact_default(self):
        return {"email": "to1@example.com"}

    contact_info = JSONField("ContactInfo", default=contact_default)

    # editable
    # 기본값 True, False로 지정시 ModelForm에서 admin이나 누구에게도 보이지 않는다
    # 또한 값 검증(validation)도 스킵한다
    a = models.CharField(editable=False)

    # error_messages
    # 오류 메시지는 null, blank, invalid, invalid_choice, unique,와 unique_for_date가 포함된다
    # 필드 유형 섹션의 각 필드에 대해 추고 오류 메시지 키가 지정된다
    # 다음은 forms에서 사용된 예시이다
    # 참조
    # https://docs.djangoproject.com/ko/3.1/topics/forms/modelforms/#considerations-regarding-model-errormessages
    class ArticleForm(ModelForm):
        class Meta:
            error_messages = {
                NON_FIELD_ERRORS: {
                    'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
                }
            }

    # help_text
    # 텍스트가 양식 위젯과 함께 표시된다
    # 원하는 경우 HTML을 포함 할 수 있다
    a = models.CharField(help_text="help text : <div>html code</div>")

    # primary_key
    # primary_key=True인 경우 모델의 기본 키, 기본키는 읽기 전용이다
    # 지정하지 않으면 AutoField 기본 키를 자동으로 추가한다
    # primary_key는 null=false, unique=true를 의미한다
    # 개체에 기본기 1개만 허용
    a = models.CharField(primary_key=True)
    # 자동 기본 키 필드 참조
    # https://docs.djangoproject.com/ko/3.1/topics/db/models/#automatic-primary-key-fields

    # unique
    # Ture인 경우 이 필드는 테이블에 고유해야한다
    # 중복값을 save()하려고 하면  save()메소드에서 django.db.IntegrityError 에러 발생
    # 이 옵션은 MTM, OTO필드를 제외한 모든 유형에서 유효한다
    # unique가 True이면 db_index를 지정할 필요가 없다, index생성을 의미하기 때문에
    a = models.CharField(unique=True)

    # unique_for_date
    # 필드가 DateField 또는 DateTimeField를 지정해야 한다
    # 예를들어 title에 unique_for_date="pub_date"가 있으면
    # 동일 title에 동일한 pub_date가 있을 수 없다
    # 날짜 시간 필드를 가리키도록 설정할 경우 필드의 날짜 부분만 고려한다
    # settings의 USE_TZ가 True이면 객체가 저장될 때 현재 표준 시간대에서 검사
    # 이 작업은 Model.validate_unique()에 의해 수행되지만 데이터베이스 수준에서는 수행하지 않는다
    # unique_for_date 조건이 모델 양식에 속하지 않는 필드와 관련된 경우(예시), 유효성 검사를 건너뛴다
    # 예시(필드중 하나가 제외되거나 editable=false 일 때)
    a = models.CharField(unique_for_date="pub_date")

    # unique_for_month
    # unique_for_date와 같으나 month가 unique
    a = models.CharField(unique_for_date="pub_date")

    # unique_for_year
    # unique_for_date, month와 같으나 year 가unique
    a = models.CharField(unique_for_date="pub_date")

    # validators
    # 필드에 대해 실행할 유효성 검사기
    # 지원되는 Validators 목록 https://docs.djangoproject.com/ko/3.1/ref/validators/
    # Validators는 함수 형태로 만들어서 추가 하거나 목록에서 가져와서 쓰면 된다
    # forms 딴에서도 validator를 쓸 수 있다
    def validate_even(self, value):
        pass
    a = models.CharField(validators=[valdate_even])


