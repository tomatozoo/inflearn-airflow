from airflow.sensors.base import BaseSensorOperator
from airflow.hooks.base import BaseHook


class SeoulApiDateSensor(BaseSensorOperator):
    template_fields = ('endpoint',)

    def __init__(self, dataset_nm, base_dt_col, day_off=0, **kwargs):
        super().__init__(**kwargs)
        self.http_conn_id = 'openapi.seoul.go.kr'
        self.endpoint = '{{var.value.apikey_openapi_seoul_go_kr}}/json/' + dataset_nm + '/1/100'
        self.day_off = day_off
        self.base_df_col = base_dt_col

    def poke(self, context):
        import requests
        import json
        from dateutil.relativedelta import relativedelta
        connection = BaseHook.get_connection(self.http_conn_id)
        url = f'http://{connection.host}:{connection.port}/{self.endpoint}'
        self.log.info(f'request url: {url}')
        response = requests.get(url)

        contents = json.loads(response.text)
        key_nm = list(contents.keys())[0]
        row_data = contents.get(key_nm).get('row')
        last_dt = row_data[0].get(self.base_dt_col)
        last_date = last_dt[:10]
        last_date = last_date.replace('.', '-').replace('/', '-')
        search_ymd = (context.get('data_interval_end').in_timezone('Asia/Seoul') + relativedelta(days=self.day_off)).strftime('YYYY-MM-DD')
        try:
            import pendulum
            pendulum.from_format(last_date, 'YYYY-MM-DD')
        except:
            from airflow.exceptions import AirflowException
            AirflowException(f'{self.base_dt_col} 칼럼은 YYYY.MM.DD 도는 YYYY/MM/DD 형태가 아닙니다')
        
        if last_date >= search_ymd:
            self.log.info(f'생성 확인()')
            return True
        else:
            self.log.info("")
            return False
