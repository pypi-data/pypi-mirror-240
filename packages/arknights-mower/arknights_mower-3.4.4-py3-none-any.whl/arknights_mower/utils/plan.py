class Plan(object):

    def __init__(self, plan, config, trigger=None, task=None):
        # 基建计划 or 触发备用plan 的排班表，只需要填和默认不一样的部分
        self.plan = plan
        # 基建计划相关配置，必须填写全部配置
        self.config = config
        # 触发备用plan 的条件(必填）就是每次最多只有一个备用plan触发
        self.trigger = trigger
        # 触发备用plan 的时间生成的任务 (选填）
        self.task = task


class Room(object):

    def __init__(self, agent, group, replacement):
        # 固定高效组干员
        self.agent = agent
        # 分组
        self.group = group
        # 替换组
        self.replacement = replacement


def to_list(str_data):
    lst = str_data.replace('，', ',').split(',')
    return [x.strip() for x in lst]


class PlanConfig(object):
    # run_order_buffer_time: 
    #   >  0 时是葛朗台跑单
    #   <= 0 时是无人机跑单
    def __init__(self, rest_in_full, exhaust_require, resting_priority, ling_xi=0, workaholic="", max_resting_count=4,
                 free_blacklist="", read_mood=True, skip_validation=False, run_order_buffer_time=30,
                 resting_threshold=0.5, refresh_trading_config=''):
        self.rest_in_full = to_list(rest_in_full)
        self.exhaust_require = to_list(exhaust_require)
        self.workaholic = to_list(workaholic)
        self.resting_priority = to_list(resting_priority)
        self.max_resting_count = max_resting_count
        self.free_blacklist = to_list(free_blacklist)
        self.read_mood = read_mood
        # 0 为均衡模式
        # 1 为感知信息模式
        # 2 为人间烟火模式
        self.ling_xi = ling_xi
        self.skip_validation = skip_validation
        self.run_order_buffer_time = run_order_buffer_time
        self.resting_threshold = resting_threshold
        # 格式为 干员名字+ 括弧 +指定房间（逗号分隔）
        # 不指定房间则默认全跑单站
        # example： 阿米娅,夕,令
        #           夕(room_3_1,room_1_3),令(room_3_1)
        self.refresh_trading_config = [e.strip() for e in refresh_trading_config.split(',')]

    def get_config(self, agent_name, config_type):
        if config_type == 0:
            return agent_name in self.rest_in_full
        elif config_type == 1:
            return agent_name in self.exhaust_require
        elif config_type == 2:
            return agent_name in self.workaholic
        elif config_type == 3:
            return agent_name in self.resting_priority
        elif config_type == 4:
            return agent_name in self.free_blacklist
        elif config_type == 5:
            match = next((e for e in self.refresh_trading_config if agent_name in e.lower()), None)
            if match is not None:
                if match.replace(agent_name, '') != '':
                    return [True, match.replace(agent_name, '').split(',')]
                else:
                    return [True, []]
            else:
                return [False, []]
