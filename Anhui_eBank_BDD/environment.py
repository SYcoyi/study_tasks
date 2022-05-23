# -*- coding: UTF-8 -*-
"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)
++++++++++++++++++++++++++++++++++++++++++++++++++++
run operation
before_all
for feature in all_features:
    before_feature
    for scenario in feature.scenarios:
        before_scenario
        for step in scenario.steps:
            before_step
                step.run()
            after_step
        after_scenario
    after_feature
after_all

"""

import logging
from config_template import BASE_CONFIG

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=BASE_CONFIG['LOG']['LOG_FILE_NAME'],
                    filemode='w')

def before_all(context):
    logging.info('-------before_all-------------')

def after_all(context):
    logging.info('-------all_finished-------------')

def before_scenario(context, scenario):
    print('-------before_scenario-------------')
    with open('http_result/' + 'scenario' + str(id(scenario)) + '.json', 'a+') as f:
        scen = {
            'name': scenario.name,
            'steps_count': str(len(scenario.steps)),
            'skip_reason': scenario.skip_reason,
            'error_message': scenario.error_message
        }
        f.write(str(scen) + '\n')
def before_step(context, step):
    logging.info('-------before_step-------------')
    logging.info(step.name)
    context.current_step = step



def clean_temp_folder():
    '''
    清除临时文件夹
    '''
    temp_folders = [
        BASE_CONFIG['REPORT_FOLDER'],
        BASE_CONFIG['ALLURE_REPORT_FOLDER'],
        BASE_CONFIG['TEMP_FOLDER'],
    ]