from enum import Enum

class BudgetExceedPolicy(Enum): 
    POLICY_NO_LIMIT = 'NO_LIMIT'
    POLICY_STOP_ENTRY = 'STOP_ENTRY'
    POLICY_FIFO = 'FIFO'
    POLICY_WORST = 'WORST'