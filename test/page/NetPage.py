from selenium.webdriver import Keys

from test.page.BasePage import BasePage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import time
import re

logger = Logger(logger="NetPage").getlog()


class NetPage(BasePage):
    left_net_manage = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/a[3]/div")
    left_sec_base_net = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[1]/a")
    left_sec_port = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[2]/a")
    left_sec_route = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[3]/a")
    left_sec_dns = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[4]/a")
    left_sec_vlan = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[5]/a")
    left_sec_net_console = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/ul[3]/li[6]/a")

    right_ok_btn = (By.CSS_SELECTOR, ".button2")

    right_base_net_mode_radio = (By.ID, 'mode_sign')
    right_base_net_mode_radio_all = (By.XPATH, "//input[@id='mode_sign']")
    right_base_net_mode_radio_double = (By.XPATH, '//*[@id="mode_sign" and @value="0"]')
    right_base_net_mode_radio_sigle = (By.XPATH, '//*[@id="mode_sign" and @value="1"]')
    right_base_net_mode_radio_bridge = (By.XPATH, '//*[@id="mode_sign" and @value="2"]')
    right_base_net_set_ip1 = (By.ID, "NM_Ip0")
    right_base_net_set_netmask1 = (By.ID, "NM_Netmask0")
    right_base_net_set_gateway1 = (By.ID, "NM_Gateway0")
    right_base_net_set_mtu1 = (
        By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[3]/table/tbody/tr[6]/td[1]/span[2]/input[1]")
    right_base_net_set_ip2 = (By.ID, "NM_Ip1")
    right_base_net_set_netmask2 = (By.ID, "NM_Netmask1")
    right_base_net_set_gateway2 = (By.ID, "NM_Gateway1")
    right_base_net_set_mtu2 = (
        By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[3]/table/tbody/tr[6]/td[2]/span[2]/input[1]")
    right_base_net_set_ip3 = (By.ID, "NM_Ip2")
    right_base_net_set_netmask3 = (By.ID, "NM_Netmask2")
    right_base_net_set_gateway3 = (By.ID, "NM_Gateway2")
    right_base_net_set_mtu3 = (
        By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[4]/div/table/tbody/tr[2]/td[4]/span[2]/input[1]")
    right_base_net_set_ip4 = (By.ID, "NM_Ip3")
    right_base_net_set_netmask4 = (By.ID, "NM_Netmask3")
    right_base_net_set_gateway4 = (By.ID, "NM_Gateway3")
    right_base_net_set_mtu4 = (
        By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[5]/div/table/tbody/tr[2]/td[4]/span[2]/input[1]")
    right_base_net_save = (By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td[1]/input")
    right_base_net_applicate = (
        By.XPATH, "/html/body/div[1]/form/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td[2]/input")

    right_port_proxy = (By.ID, "port_proxy")
    right_port_manage = (By.ID, "port_cfg")
    right_port_white = (By.ID, "port_mt")
    right_port_out = (By.ID, "port_out")

    right_route_add_btn = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[1]/a[1]/span")
    right_route_del_btn = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[1]/a[2]/span")
    right_route_subnet_name = (
        By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[1]/span/input[1]")
    right_route_search_btn = (
        By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[1]/span/span/a")
    right_route_add_subnet = (By.ID, "NM_Subnet")
    right_route_add_netmask = (By.ID, "NM_Netmask")
    right_route_add_gateway = (By.ID, "NM_Gateway")
    # 弹出框操作成功关闭按钮
    right_route_add_ok_btn = (By.XPATH, "/html/body/div[2]/div[3]/a[1]")##dlgresult-buttons > a:nth-child(1) > span:nth-child(1)
    right_route_add_close_btn = (By.CSS_SELECTOR, "div.panel:nth-child(5) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
    right_route_add_cancel_btn = (By.XPATH, "/html/body/div[2]/div[3]/a[2]")
    # 路由选中的checkbox
    right_route_add_check_box = (By.XPATH, "//input[@type='checkbox']")
    # 路由界面中的总记录
    right_route_total_records = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[3]/div[1]")
    # 路由界面下一页按钮
    right_route_next_page = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr/td[10]/a")
    right_route_page_input = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr/td[7]/input")


    right_dns_dns_address1 = (By.ID, "DNS_Ip")
    right_dns_dns_address2 = (By.ID, "DNS_Ip_bak")

    right_vlan_add_btn = (By.XPATH, "/html/body/div[1]/form/div/table/tbody/tr[2]/td/div/div/div/div[1]/a[1]/span")
    iframe_css = (By.CSS_SELECTOR, "#mainid > iframe:nth-child(1)")

    right_success = (By.XPATH, "/html/body/div[2]/div[2]/form/center/div/table/tbody/tr/td/span")
    right_dialog_close_btn = (By.XPATH, "/html/body/div[2]/div[3]/a")

    def change_net_mode(self, modeType, ip_dict=None):
        """
        更改部署模式
        :param modeType:0 双臂， 1 单臂， 2 网桥
        :param ip_dict:传入IP字典，如果modeType为0 则需要传入此参数。形如{“ip”:"", "netmask"}
        :rtype: object
        """
        self.click_sec_left(self.left_net_manage, self.left_sec_base_net)
        self.switch_to_frame(self.find_element(self.iframe_css))
        # 查看当前元素是否被选中
        if self.find_element(self.right_base_net_mode_radio_sigle).is_selected():
            three_ip_flag = 1
        elif self.find_element(self.right_base_net_mode_radio_bridge).is_selected():
            three_ip_flag = 1
        else:
            three_ip_flag = 0
        # 如果要从三个网卡切换到4个网卡时，需要给定第四个ip参数
        if modeType == 0 and three_ip_flag == 1:
            self.find_element(self.right_base_net_mode_radio_double).click()
            if len(ip_dict) != 0 and "ip" in ip_dict:
                if "ip" in ip_dict["ip"]:
                    self.clear(self.right_base_net_set_ip4)
                    self.send_key(self.right_base_net_set_ip4, ip_dict.get("ip"))
                if "netmask" in ip_dict["ip"]:
                    self.clear(self.right_base_net_set_netmask4)
                    self.send_key(self.right_base_net_set_netmask4, ip_dict.get("netmask"))
                if "mtu" in ip_dict["ip"]:
                    self.clear(self.right_base_net_set_mtu4)
                    self.send_key(self.right_base_net_set_mtu4, ip_dict.get("mtu"))
                if "gateway" in ip_dict["ip"]:
                    self.clear(self.right_base_net_set_gateway4)
                    self.send_key(self.right_base_net_set_gateway4, ip_dict.get("gateway"))
            else:
                # self.clear(self.right_base_net_set_ip4)
                self.send_key(self.right_base_net_set_ip4, "192.168.111.111")
                # self.clear(self.right_base_net_set_netmask4)
                self.send_key(self.right_base_net_set_netmask4, "255.255.255.0")
                # self.clear(self.right_base_net_set_mtu4)
                self.send_key(self.right_base_net_set_mtu4, "1500")
                logger.warning("需要传递IP参数，当前无传递的IP参数，使用默认192.168.111.111/24 填充")
        elif modeType == 1:
            self.find_element(self.right_base_net_mode_radio_sigle).click()
        elif modeType == 2:
            self.find_element(self.right_base_net_mode_radio_bridge).click()
        else:
            logger.error("no such modeType, please input 0  or 1 or 2")
        self.find_element(self.right_base_net_applicate).click()
        self.click_alert()
        time.sleep(10)
        self.find_element(self.right_success)
        time.sleep(15)
        # 关闭窗口

    def change_base_net(self, modeType, ip_dict):
        """
        修改网络ip地址
        :param modeType:0 双臂， 1 单臂， 2 网桥
        :param ip_dict:
        :rtype: object
        """
        self.click_sec_left(self.left_net_manage, self.left_sec_base_net)
        self.switch_to_frame(self.find_element(self.iframe_css))
        if "ip1" not in ip_dict or "ip2" not in ip_dict or "ip3" not in ip_dict:
            logger.warning("传入的ip参数命名错误或缺少对应ip参数，将不对ip参数进行修改")
        else:
            if "ip1" in ip_dict:
                if "ip" in ip_dict["ip1"]:
                    self.clear(self.right_base_net_set_ip1)
                    self.send_key(self.right_base_net_set_ip1, ip_dict.get("ip1").get("ip"))
                if "netmask" in ip_dict["ip1"]:
                    self.clear(self.right_base_net_set_netmask1)
                    self.send_key(self.right_base_net_set_netmask1,
                                  ip_dict.get("ip1").get("netmask"))
                if "mtu" in ip_dict["ip1"]:
                    self.clear(self.right_base_net_set_mtu1)
                    self.send_key(self.right_base_net_set_mtu1, ip_dict.get("ip1").get("mtu"))
                if "gateway" in ip_dict["ip1"]:
                    self.clear(self.right_base_net_set_gateway1)
                    self.send_key(self.right_base_net_set_gateway1,
                                  ip_dict.get("ip1").get("gateway"))
            if "ip2" in ip_dict:
                if "ip" in ip_dict["ip2"]:
                    self.clear(self.right_base_net_set_ip2)
                    self.send_key(self.right_base_net_set_ip2, ip_dict.get("ip2").get("ip"))
                if "netmask" in ip_dict["ip2"]:
                    self.clear(self.right_base_net_set_netmask2)
                    self.send_key(self.right_base_net_set_netmask2,
                                  ip_dict.get("ip2").get("netmask"))
                if "mtu" in ip_dict["ip2"]:
                    self.clear(self.right_base_net_set_mtu2)
                    self.send_key(self.right_base_net_set_mtu2, ip_dict.get("ip2").get("mtu"))
                if "gateway" in ip_dict["ip2"]:
                    self.clear(self.right_base_net_set_gateway2)
                    self.send_key(self.right_base_net_set_gateway2,
                                  ip_dict.get("ip2").get("gateway"))
            if "ip3" in ip_dict:
                if "ip" in ip_dict["ip3"]:
                    self.clear(self.right_base_net_set_ip3)
                    self.send_key(self.right_base_net_set_ip3, ip_dict.get("ip3").get("ip"))
                if "netmask" in ip_dict["ip3"]:
                    self.clear(self.right_base_net_set_netmask3)
                    self.send_key(self.right_base_net_set_netmask3,
                                  ip_dict.get("ip3").get("netmask"))
                if "mtu" in ip_dict["ip3"]:
                    self.clear(self.right_base_net_set_mtu3)
                    self.send_key(self.right_base_net_set_mtu3, ip_dict.get("ip3").get("mtu"))
                if "gateway" in ip_dict["ip3"]:
                    self.clear(self.right_base_net_set_gateway3)
                    self.send_key(self.right_base_net_set_gateway3,
                                  ip_dict.get("ip3").get("gateway"))
            if "ip4" in ip_dict:
                if modeType == 0:
                    if "ip" in ip_dict["ip4"]:
                        self.clear(self.right_base_net_set_ip4)
                        self.send_key(self.right_base_net_set_ip4, ip_dict.get("ip4").get("ip"))
                    if "netmask" in ip_dict["ip4"]:
                        self.clear(self.right_base_net_set_netmask4)
                        self.send_key(self.right_base_net_set_netmask4,
                                      ip_dict.get("ip4").get("netmask"))
                    if "mtu" in ip_dict["ip4"]:
                        self.clear(self.right_base_net_set_mtu4)
                        self.send_key(self.right_base_net_set_mtu4, ip_dict.get("ip4").get("mtu"))
                    if "gateway" in ip_dict["ip4"]:
                        self.clear(self.right_base_net_set_gateway4)
                        self.send_key(self.right_base_net_set_gateway4,
                                      ip_dict.get("ip4").get("gateway"))
                # else:
                #     logger.error("传入的modeType参数与传入的ip参数不一致，请检查参数")
            else:
                logger.warning("找不到传入的ip参数")

        self.find_element(self.right_base_net_applicate).click()
        self.click_alert()
        time.sleep(15)
        # 切换窗口
        tt = self.find_element(self.right_success)
        print(tt.text)
        time.sleep(3)
        self.find_element(self.right_dialog_close_btn).click()

    def change_port(self, *port_list):
        self.click_sec_left(self.left_net_manage, self.left_sec_port)
        self.switch_to_frame(self.find_element(self.iframe_css))
        lp = len(port_list)
        if lp == 0:
            logger.warning("传入的配置端口参数为空")
        else:
            self.send_key(self.right_port_proxy, port_list[0])
            if lp >= 2:
                self.send_key(self.right_port_manage, port_list[1])
                if lp >= 3:
                    self.send_key(self.right_port_white, port_list[2])
                    if lp == 4:
                        self.send_key(self.right_port_out, port_list[3])
                    else:
                        logger.warning("传入的配置端口参数个数超过4个，仅填充前4个")
        self.find_element(self.right_ok_btn).click()

    def route_add(self, route_dict):
        """
        增加路由函数
        输入的参数为接收多个dict，形如：{“subnet”：“192.168.1.11”， “netmask”：“255.255.255.255”， “gateway“：”192.168.1.1“}
        :param route_dict: dict的list[{“subnet”：“192.168.1.11”， “netmask”：“255.255.255.255”， “gateway“：”192.168.1.1“},
        {“subnet”：“192.168.1.12”， “netmask”：“255.255.255.255”， “gateway“：”192.168.1.1“}]
        :rtype: object
        """
        self.click_sec_left(self.left_net_manage, self.left_sec_route)
        self.switch_to_frame(self.find_element(self.iframe_css))
        # 如果传入参数不为空
        #   则点击增加按钮
        #   for i in list
        #       if subnet netmask gateway都存在
        #           则点击增加按钮
        #           填入以上内容
        #           点击确定按钮
        #           等待3秒
        #           如果为alert
        #               如果为alert则关闭alert
        #               输出错误日志
        #           如果不是alert
        #               关闭弹框
        # 如果传入的参数为空
        #   输出日志
        if len(route_dict):
            for r in route_dict:
                if "subnet" in r and "netmask" in r and "gateway" in r:
                    self.find_element(self.right_route_add_btn).click()
                    self.send_key(self.right_route_add_subnet, r["subnet"])
                    self.send_key(self.right_route_add_netmask, r["netmask"])
                    self.send_key(self.right_route_add_gateway, r["gateway"])
                    self.find_element(self.right_route_add_ok_btn).click()
                    time.sleep(3)
                    if self.is_alert_present() is None:
                        self.click_alert()
                        logger.warning("传入的参数无法被添加到现有路由")
                    else:
                        self.find_element(self.right_route_add_close_btn).click()
                else:
                    logger.warning("传入的路由参数不对，请检查路由参数")
        else:
            logger.warning("传入的路由参数为空，请检查路由参数")


    def route_del(self, del_all, del_list):
        """

        :param del_all: 如果为0 表示删除del_list中index的条目，如果为1则全部删除
        :param del_list: 删除的第几条（1,2,4,5,11）表示删除第1,2,4,5,11条
        """
        self.click_sec_left(self.left_net_manage, self.left_sec_route)
        self.switch_to_frame(self.find_element(self.iframe_css))
        ck_all = self.find_elements(self.right_route_add_check_box)
        ck_num = len(ck_all)
        #如果为全选
        if del_all:
            ck_all[0].click()
        else:
            del_len = len(del_list)
            record_string = self.find_element(self.right_route_total_records).text
            #通过正则表达式取所有数字，然后取最后一个数字,转为int类型
            record_num = int(re.compile(r'\d+').findall(record_string)[-1])
            if del_len:
                for del_num in del_list:
                    if del_num <= record_num:
                        if del_num <= 10:
                            ck_all[del_num+1].click()# 从标题checkbox的下一行开始
                        else:
                            page_num = del_num / 10
                            new_index = del_num % 10
                            # 翻页
                            self.send_key(self.right_route_page_input, page_num).send_keys(Keys.ENTER)
                            time.sleep(3)
                            ck_all = self.find_elements(self.right_route_add_check_box)
                            ck_all[new_index+1].click()
                            ck_all = self.send_key(self.right_route_page_input, 1).send_keys(Keys.ENTER)
                    else:
                        logger.warning("给定del_list中的index超出记录数")
            else:
                logger.warning("给定del_list中没有参数")
        self.find_element(self.right_route_del_btn).click()



        # 获取checkbox中所有checkbox
        # 获取全部记录
        # 遍历del_len中的所有元素
        #   如果del_num 中元素大于ck_num-1（需减掉标题中的checkbox）则直接打warning日志
        #   如果del_num 中元素小于ck_num-1
        #       如果del_num < 10
        #           选中ck(del_num)
        #       如果del_num > 10
        #           进行翻页
        #           选中ck(del_num)


if __name__ == '__main__':
    np = NetPage('firefox')
    np.get("http://192.168.1.111:7789/fortest?key=CN=admin,OU=XA,O=SDT,C=CN")
    # np.change_net_mode(0, {})
    ip1_dict = {"ip": "192.168.10.168", "netmask": "255.255.255.0", "mtu": "1500"}
    ip_dict = {"ip1": ip1_dict, "ip2": "", "ip3": "", "ip4": ""}
    # np.change_base_net(2, ip_dict)
    # np.route_del(0,())
    # add route test
    ip_dict = []
    for i in range (0,22):
        tmp_dict = {}
        ip_s = i + 22
        tmp_dict["subnet"] = "192.168.10." + str(ip_s)
        tmp_dict["netmask"] = "255.255.255.255"
        tmp_dict["gateway"] = "192.168.10.1"
        ip_dict.append(tmp_dict)
    print(ip_dict)
    np.route_add(ip_dict)
    # {"subnet":"", "netmask":"", "gateway":""}
