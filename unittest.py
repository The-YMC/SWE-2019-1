# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import ymap

class TestMap(ymap.Map):
    """
    Map의 child class
    Map list의 element를 수정할 수 있는 method가 추가됨.
    """
    def modify(self, map_index, user_info, n_piece):     
        self.map_list[map_index][2] = user_info
        self.map_list[map_index][3] = n_piece
        self.user_remained[user_info] = self.user_remained[user_info] - n_piece
    

class TestLogic():
    """
    윷판의 말이 제대로 도착했는지 확인하는 Unit Test Class
    """
    def assertEqual(self, x, y):
        if x != y:
            raise AssertionError("Error")
    
    def parting_path1(self, user_info, n_roll, n_piece):
        """
        5번 갈림길에서 윷판을 던졌을 때, 제대로 말이 도착하는지 확인.
        """
        tmap = TestMap()
        tmap.modify(5, user_info, n_piece)
        map_result , _ , _ , _ = tmap.select(n_roll, 5, user_info)
        if n_roll != 3:
            if n_roll in [4,5]:
                n_roll = n_roll - 1
            self.assertEqual(map_result[19+n_roll][2], user_info)
            self.assertEqual(map_result[19+n_roll][3], n_piece)
        elif n_roll == 3:
            self.assertEqual(map_result[28][2], user_info)
            self.assertEqual(map_result[28][3], n_piece)
        
    def parting_path2(self, user_info, n_roll, n_piece):
        """
        10번 갈림길에서 윷판을 던졌을 때, 제대로 말이 도착하는지 확인.
        """
        tmap = TestMap()
        tmap.modify(10, user_info, n_piece)
        map_result , _ , _ , _ = tmap.select(n_roll, 10, user_info)
        if n_roll != 3:
            if n_roll in [4,5]:
                n_roll = n_roll - 1
            self.assertEqual(map_result[23+n_roll][2], user_info)
            self.assertEqual(map_result[23+n_roll][3], n_piece)
        elif n_roll == 3:
            self.assertEqual(map_result[28][2], user_info)
            self.assertEqual(map_result[28][3], n_piece)
    
    def parting_path3(self, user_info, n_roll, n_piece):
        """
        22번에서 15번을 넘어가는 갈림길에서, 제대로 말이 도착하는지 확인.
        """
        tmap = TestMap()
        tmap.modify(22, user_info, n_piece)
        map_result , _ , _ , _ = tmap.select(n_roll, 22, user_info)
        if n_roll == 1:
            self.assertEqual(map_result[23][2], user_info)
            self.assertEqual(map_result[23][3], n_piece)
        else:
            self.assertEqual(map_result[13 + n_roll][2], user_info)
            self.assertEqual(map_result[13 + n_roll][3], n_piece)
    
    def parting_path4(self, user_info, n_roll, n_piece):
        """
        28번에 있을 때, 제대로 말이 도착하는지 확인. 
        """
        
        tmap = TestMap()
        tmap.modify(28, user_info, n_piece)
        map_result , _ , _ , in_goal = tmap.select(n_roll, 28, user_info)
        if n_roll < 3:
            self.assertEqual(map_result[25 + n_roll][2], user_info)
            self.assertEqual(map_result[25 + n_roll][3], n_piece)
        if n_roll == 3:
            self.assertEqual(map_result[0][2], user_info)
            self.assertEqual(map_result[0][3], n_piece)
        else:
            self.assertEqual(in_goal[user_info], n_piece)
            self.assertEqual(in_goal[user_info], n_piece)
    
    def is_goal(self, user_info, n_piece):
        """
        goal에 윷판이 제대로 들어가는지 확인.
        """
        tmap = TestMap()
        tmap.modify(0, user_info, n_piece)
        self.assertEqual(tmap.select(1, 0, user_info)[3][user_info], n_piece)


    def catch(self, user_info1, n_piece1, user_info2, n_piece2):
        """
        말이 상대방의 윷판을 제대로 잡는지 확인.
        말을 잡고 윷을 한번 더 던지는지 확인.
        잡힌 상대방 말은 시작점으로 돌아가는지 확인.
        """
        tmap = TestMap()
        tmap.modify(5, user_info2, n_piece2)
        tmap.modify(4, user_info1, n_piece1)
        map_result, remained, turn, _ = tmap.select(1, 4, user_info1)
        self.assertEqual(map_result[5][2], user_info1)
        self.assertEqual(map_result[5][3], n_piece1)
        self.assertEqual(remained[user_info2], 4)
        self.assertEqual(turn, user_info1)
        
    def back_do1(self, user_info, n_piece):
        """
        직전에 25번 방향에서 28번으로 넘어갔을 때, 백도가 25번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(25, user_info, n_piece)
        tmap.select(1, 25, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 28, user_info)
        self.assertEqual(map_result[25][2], user_info)
        self.assertEqual(map_result[25][3], n_piece)
        
    def back_do2(self, user_info, n_piece):
        """
        직전에 21번 방향에서 28번으로 넘어갔을 때, 백도가 25번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(21, user_info, n_piece)
        tmap.select(1, 21, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 28, user_info)
        self.assertEqual(map_result[21][2], user_info)
        self.assertEqual(map_result[21][3], n_piece)
        
    def back_do3(self, user_info, n_piece):
        """
        직전에 14번 방향에서 15번으로 넘어갔을 때, 백도가 14번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(14, user_info, n_piece)
        tmap.select(1, 14, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 15, user_info)
        self.assertEqual(map_result[14][2], user_info)
        self.assertEqual(map_result[14][3], n_piece)
        
    def back_do4(self, user_info, n_piece):
        """
        직전에 23번 방향에서 15번으로 넘어갔을 때, 백도가 23번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(23, user_info, n_piece)
        tmap.select(1, 23, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 15, user_info)
        self.assertEqual(map_result[23][2], user_info)
        self.assertEqual(map_result[23][3], n_piece)
    
    def back_do5(self, user_info, n_piece):
        """
        24번에서 백도를 했을 때, 10번으로 돌아가는지 확인.
        """
        tmap = TestMap()
        tmap.modify(24, user_info, n_piece)
        map_result, _ , _ , _ = tmap.select(-1, 24, user_info)
        self.assertEqual(map_result[10][2], user_info)
        self.assertEqual(map_result[10][3], n_piece)
    
    def back_do6(self, user_info, n_piece):
        """
        20번에서 백도를 했을 때, 5번으로 돌아가는지 확인.
        """
        tmap = TestMap()
        tmap.modify(20, user_info, n_piece)
        map_result, _ , _ , _ = tmap.select(-1, 20, user_info)
        self.assertEqual(map_result[5][2], user_info)
        self.assertEqual(map_result[5][3], n_piece)
    
    def back_do7(self, user_info, n_piece):
        """
        직전에 19번 방향에서 0번으로 넘어갔을 때, 백도가 19번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(19, user_info, n_piece)
        tmap.select(1, 19, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 0, user_info)
        self.assertEqual(map_result[19][2], user_info)
        self.assertEqual(map_result[19][3], n_piece)
    
    def back_do8(self, user_info, n_piece):
        """
        직전에 27번 방향에서 0번으로 넘어갔을 때, 백도가 27번으로 되는지 확인.
        """
        tmap = TestMap()
        tmap.modify(27, user_info, n_piece)
        tmap.select(1, 27, user_info)
        map_result, _ , _ , _ = tmap.select(-1, 0, user_info)
        self.assertEqual(map_result[27][2], user_info)
        self.assertEqual(map_result[27][3], n_piece)

