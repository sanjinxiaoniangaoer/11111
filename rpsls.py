#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ⶫѸ
���ڣ�2022��5��10��
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    if name=="ʷ����":
        return 1
    if name=="ֽ":
        return 2
    if name=="����":
        return 3
    if name=="����":
        return 4


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    if number==1:
        return "ʷ����"
    if number==2:
        return "ֽ"
    if number==3:
        return "����"
    if number==4:
        return "����"
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice=str(input("����������ѡ�����:"))
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    print("�������ѡ��Ϊ��%s"%number_to_name(comp_number))

    if player_choice_number==0 and comp_number==4 or 3:
        return print("��Ӯ��")
    if player_choice_number==1 and comp_number==0 or 4:
        return print("��Ӯ��")
    if player_choice_number==2 and comp_number==0 or 1:
        return print("��Ӯ��")
    if player_choice_number==3 and comp_number==1 or 2:
        return print("��Ӯ��")
    if player_choice_number==4 and comp_number==2 or 3:
        return print("��Ӯ��")
    elif player_choice_number==comp_number:
        return print("���ͼ��������һ����")
    else:
        return "�����Ӯ��"



    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
