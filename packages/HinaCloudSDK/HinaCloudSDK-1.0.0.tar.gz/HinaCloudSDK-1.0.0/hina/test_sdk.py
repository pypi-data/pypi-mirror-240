import time
import unittest

from hina.sdk import HinaCloudSDK

url = "https://test-hicloud.hinadt.com/gateway/hina-cloud-engine/ha?project=yituiAll&token=yt888"


class NormalTest(unittest.TestCase):

    def test_singleton(self):
        HinaCloudSDK.init(url, 2)
        HinaCloudSDK.init(url, 3)

    def test_dev(self):
        hina_sdk = HinaCloudSDK.init(url, 2, True)
        # 设置全局属性
        hina_sdk.register_super_properties({'H_os': 'macos', 'H_os_version': 'ventura'})
        # 发送事件，未登录
        anonymous_id = str(int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event',
                            {'cat_name': 'san', 'pay_type': 'online999', 'H_lib': 'Java'}, False,
                            int(time.time() * 1000))
        hina_sdk.close()

    def test_normal(self):
        hina_sdk = HinaCloudSDK.init(url, 2)
        # 设置全局属性
        hina_sdk.register_super_properties({'H_os': 'macos', 'H_os_version': 'ventura'})

        # 发送事件，未登录
        anonymous_id = str(int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online999'}, False,
                            int(time.time() * 1000))
        # 登录并绑定用户ID
        account_id = str(int(time.time() * 1000))
        hina_sdk.bind_id(account_id, anonymous_id)

        # 设置用户属性
        data = {
            'name': 'sansan819',
            'age': 33,
            'sex': 'male',
            'birth': '1991-02-05 11:22:33'
        }
        hina_sdk.user_set(account_id, data)

        # 登录后发送事件
        hina_sdk.send_event(account_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online991'}, True,
                            int(time.time() * 1000))
        hina_sdk.send_event(account_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online992'}, True,
                            int(time.time() * 1000))
        hina_sdk.send_event(account_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online993'}, True,
                            int(time.time() * 1000))
        hina_sdk.send_event(account_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online994'}, True,
                            int(time.time() * 1000))

        # 固定初始值的属性，首次设置(如果不存在则设置，存在就不设置)
        data = {
            'name': 'Sansan819',
            'company_name': 'haina啊',
        }
        hina_sdk.user_set_once(account_id, data)

        data = {
            'company_name': 'haina1',
            'company_address': '上海市',
        }
        hina_sdk.user_set_once(account_id, data)

        # 对当前用户的属性做递增或者递减
        hina_sdk.user_add(account_id, 'age', 1)

        # 取消用户属性
        hina_sdk.user_unset(account_id, 'birth')

        hina_sdk.close()

    def test_batch(self):
        hina_sdk = HinaCloudSDK.init(url, 2, True)

        # 设置全局属性
        hina_sdk.register_super_properties({'H_os': 'macos', 'H_os_version': 'ventura'})
        # 发送事件，未登录
        anonymous_id = str(int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online991'}, False,
                            int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online992'}, False,
                            int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online993'}, False,
                            int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online994'}, False,
                            int(time.time() * 1000))
        hina_sdk.send_event(anonymous_id, 'python_test_event', {'cat_name': 'san', 'pay_type': 'online995'}, False,
                            int(time.time() * 1000))
        time.sleep(20)


if __name__ == '__main__':
    unittest.main()
