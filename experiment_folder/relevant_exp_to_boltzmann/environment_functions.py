import pandas as pd
import numpy as np
import tensorflow as tf

from tf_agents.environments import py_environment
from tf_agents.policies import tf_policy, tf_py_policy, py_policy
from tf_agents.trajectories import Trajectory, PolicyStep, time_step as ts
from tf_agents.specs import array_spec


class DynamicPricingCompetition():
    
    """
    A game object where the agent can interact with and that we can update remotely
    to adjust the current state based on recent observations.
    This class also keeps track of all the steps and rewards that took place for later analysis.
    """
    
    def __init__(self):
        self.selling_period = 1
        self.loadfactor = 0
        self.comp_loadfactor = 0
        self.competitor_has_capacity = 1
        self.price_competitor_t1 = 50
        self.price_competitor_t2 = 50
        self.price_competitor_t3 = 50
        self.price_competitor_t4 = 50
        self.price_competitor_t5 = 50
        self.price_competitor_t6 = 50
        self.price_competitor_t7 = 50
        self.price_competitor_t8 = 50
        self.price_competitor_t9 = 50
        self.price_competitor_t10 = 50
        self.price_t1 = 50
        self.price_t2 = 50
        self.price_t3 = 50
        self.price_t4 = 50
        self.price_t5 = 50
        self.price_t6 = 50
        self.price_t7 = 50
        self.price_t8 = 50
        self.price_t9 = 50
        self.price_t10 = 50
        self.demand_t1 = 1
        self.demand_t2 = 1
        self.demand_t3 = 1
        self.demand_t4 = 1
        self.demand_t5 = 1
        self.demand_t6 = 1
        self.demand_t7 = 1
        self.demand_t8 = 1
        self.demand_t9 = 1
        self.demand_t10 = 1
        self.demand_competitor_t1 = 1
        self.demand_competitor_t2 = 1
        self.demand_competitor_t3 = 1
        self.demand_competitor_t4 = 1
        self.demand_competitor_t5 = 1
        self.demand_competitor_t6 = 1
        self.demand_competitor_t7 = 1
        self.demand_competitor_t8 = 1
        self.demand_competitor_t9 = 1
        self.demand_competitor_t10 = 1
        self.competition_results_df = pd.DataFrame(columns=[
            'our_strategy',
            'competition_id',
            'selling_season', 
            'selling_period', 
            'competitor_id', 
            'price_competitor', 
            'price', 
            'demand', 
            'competitor_has_capacity', 
            'revenue',
            'reward'
        ])
        
        self.state = [
            self.selling_period,
            self.loadfactor,
            self.comp_loadfactor,
            self.competitor_has_capacity,
            self.price_competitor_t1,
            self.price_competitor_t2,
            self.price_competitor_t3,
            self.price_competitor_t4,
            self.price_competitor_t5,
            self.price_competitor_t6,
            self.price_competitor_t7,
            self.price_competitor_t8,
            self.price_competitor_t9,
            self.price_competitor_t10,
            self.price_t1,
            self.price_t2,
            self.price_t3,
            self.price_t4,
            self.price_t5,
            self.price_t6,
            self.price_t7,
            self.price_t8,
            self.price_t9,
            self.price_t10,
            self.demand_t1,
            self.demand_t2,
            self.demand_t3,
            self.demand_t4,
            self.demand_t5,
            self.demand_t6,
            self.demand_t7,
            self.demand_t8,
            self.demand_t9,
            self.demand_t10,
            self.demand_competitor_t1,
            self.demand_competitor_t2,
            self.demand_competitor_t3,
            self.demand_competitor_t4,
            self.demand_competitor_t5,
            self.demand_competitor_t6,
            self.demand_competitor_t7,
            self.demand_competitor_t8,
            self.demand_competitor_t9,
            self.demand_competitor_t10,
        ]
        self._reward = 0
        
    def reset(self):
        self.selling_period = 1
        self.loadfactor = 0
        self.comp_loadfactor = 0
        self.competitor_has_capacity = 1
        self.price_competitor_t1 = 50
        self.price_competitor_t2 = 50
        self.price_competitor_t3 = 50
        self.price_competitor_t4 = 50
        self.price_competitor_t5 = 50
        self.price_competitor_t6 = 50
        self.price_competitor_t7 = 50
        self.price_competitor_t8 = 50
        self.price_competitor_t9 = 50
        self.price_competitor_t10 = 50
        self.price_t1 = 50
        self.price_t2 = 50
        self.price_t3 = 50
        self.price_t4 = 50
        self.price_t5 = 50
        self.price_t6 = 50
        self.price_t7 = 50
        self.price_t8 = 50
        self.price_t9 = 50
        self.price_t10 = 50
        self.demand_t1 = 1
        self.demand_t2 = 1
        self.demand_t3 = 1
        self.demand_t4 = 1
        self.demand_t5 = 1
        self.demand_t6 = 1
        self.demand_t7 = 1
        self.demand_t8 = 1
        self.demand_t9 = 1
        self.demand_t10 = 1
        self.demand_competitor_t1 = 1
        self.demand_competitor_t2 = 1
        self.demand_competitor_t3 = 1
        self.demand_competitor_t4 = 1
        self.demand_competitor_t5 = 1
        self.demand_competitor_t6 = 1
        self.demand_competitor_t7 = 1
        self.demand_competitor_t8 = 1
        self.demand_competitor_t9 = 1
        self.demand_competitor_t10 = 1
        
        self.state = [
            self.selling_period,
            self.loadfactor,
            self.comp_loadfactor,
            self.competitor_has_capacity,
            self.price_competitor_t1,
            self.price_competitor_t2,
            self.price_competitor_t3,
            self.price_competitor_t4,
            self.price_competitor_t5,
            self.price_competitor_t6,
            self.price_competitor_t7,
            self.price_competitor_t8,
            self.price_competitor_t9,
            self.price_competitor_t10,
            self.price_t1,
            self.price_t2,
            self.price_t3,
            self.price_t4,
            self.price_t5,
            self.price_t6,
            self.price_t7,
            self.price_t8,
            self.price_t9,
            self.price_t10,
            self.demand_t1,
            self.demand_t2,
            self.demand_t3,
            self.demand_t4,
            self.demand_t5,
            self.demand_t6,
            self.demand_t7,
            self.demand_t8,
            self.demand_t9,
            self.demand_t10,
            self.demand_competitor_t1,
            self.demand_competitor_t2,
            self.demand_competitor_t3,
            self.demand_competitor_t4,
            self.demand_competitor_t5,
            self.demand_competitor_t6,
            self.demand_competitor_t7,
            self.demand_competitor_t8,
            self.demand_competitor_t9,
            self.demand_competitor_t10,
        ]
        self._reward = 0
        
    def update_state(self, vars_dict):
        self.selling_period = vars_dict['selling_period']
        self.loadfactor = vars_dict['loadfactor']
        self.comp_loadfactor = vars_dict['comp_loadfactor']
        self.competitor_has_capacity = vars_dict['competitor_has_capacity']
        self.price_competitor_t1 = vars_dict['price_competitor_t-1']
        self.price_competitor_t2 = vars_dict['price_competitor_t-2']
        self.price_competitor_t3 = vars_dict['price_competitor_t-3']
        self.price_competitor_t4 = vars_dict['price_competitor_t-4']
        self.price_competitor_t5 = vars_dict['price_competitor_t-5']
        self.price_competitor_t6 = vars_dict['price_competitor_t-6']
        self.price_competitor_t7 = vars_dict['price_competitor_t-7']
        self.price_competitor_t8 = vars_dict['price_competitor_t-8']
        self.price_competitor_t9 = vars_dict['price_competitor_t-9']
        self.price_competitor_t10 = vars_dict['price_competitor_t-10']
        self.price_t1 = vars_dict['price_t-1']
        self.price_t2 = vars_dict['price_t-2']
        self.price_t3 = vars_dict['price_t-3']
        self.price_t4 = vars_dict['price_t-4']
        self.price_t5 = vars_dict['price_t-5']
        self.price_t6 = vars_dict['price_t-6']
        self.price_t7 = vars_dict['price_t-7']
        self.price_t8 = vars_dict['price_t-8']
        self.price_t9 = vars_dict['price_t-9']
        self.price_t10 = vars_dict['price_t-10']
        self.demand_t1 = vars_dict['demand_t-1']
        self.demand_t2 = vars_dict['demand_t-2']
        self.demand_t3 = vars_dict['demand_t-3']
        self.demand_t4 = vars_dict['demand_t-4']
        self.demand_t5 = vars_dict['demand_t-5']
        self.demand_t6 = vars_dict['demand_t-6']
        self.demand_t7 = vars_dict['demand_t-7']
        self.demand_t8 = vars_dict['demand_t-8']
        self.demand_t9 = vars_dict['demand_t-9']
        self.demand_t10 = vars_dict['demand_t-10']
        self.demand_competitor_t1 = vars_dict['demand_competitor_t-1']
        self.demand_competitor_t2 = vars_dict['demand_competitor_t-2']
        self.demand_competitor_t3 = vars_dict['demand_competitor_t-3']
        self.demand_competitor_t4 = vars_dict['demand_competitor_t-4']
        self.demand_competitor_t5 = vars_dict['demand_competitor_t-5']
        self.demand_competitor_t6 = vars_dict['demand_competitor_t-6']
        self.demand_competitor_t7 = vars_dict['demand_competitor_t-7']
        self.demand_competitor_t8 = vars_dict['demand_competitor_t-8']
        self.demand_competitor_t9 = vars_dict['demand_competitor_t-9']
        self.demand_competitor_t10 = vars_dict['demand_competitor_t-10']
        
        self.state = [
            self.selling_period,
            self.loadfactor,
            self.comp_loadfactor,
            self.competitor_has_capacity,
            self.price_competitor_t1,
            self.price_competitor_t2,
            self.price_competitor_t3,
            self.price_competitor_t4,
            self.price_competitor_t5,
            self.price_competitor_t6,
            self.price_competitor_t7,
            self.price_competitor_t8,
            self.price_competitor_t9,
            self.price_competitor_t10,
            self.price_t1,
            self.price_t2,
            self.price_t3,
            self.price_t4,
            self.price_t5,
            self.price_t6,
            self.price_t7,
            self.price_t8,
            self.price_t9,
            self.price_t10,
            self.demand_t1,
            self.demand_t2,
            self.demand_t3,
            self.demand_t4,
            self.demand_t5,
            self.demand_t6,
            self.demand_t7,
            self.demand_t8,
            self.demand_t9,
            self.demand_t10,
            self.demand_competitor_t1,
            self.demand_competitor_t2,
            self.demand_competitor_t3,
            self.demand_competitor_t4,
            self.demand_competitor_t5,
            self.demand_competitor_t6,
            self.demand_competitor_t7,
            self.demand_competitor_t8,
            self.demand_competitor_t9,
            self.demand_competitor_t10,
        ]
        self._reward = 0
        
    def update_reward(self, reward):
        self.reward = reward
        
        
# Environment in which the agent operates in, and is protected from altering
class AirlineEnvironment(py_environment.PyEnvironment):
    
    def __init__(self, dpc_game, simulator, num_features, num_actions, discount, min_action, 
                 action_step, comp_sellout_price, early_termination_penalty=0, price_diff_penalty=0, 
                 loadactor_diff_penalty=0, stock_remainder_penalty=0, print_step=False):
        """
        Initialize what actions the agent can take,
        and what the observation space will look like.
        
        Also initialize the environment where the agent will interact with.
        """
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=num_actions-1, name='action'
        )
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(num_features,), dtype=np.int32, name='observation'
        )
        self._selling_season = 1
        self._episode_ended = False
        self._discount = discount
        self._dpc_game = dpc_game
        self._simulator = simulator
        self._comp_strat = np.random.choice(
            a=["random_ranges", "highstart_randomranges", "follower_strategy", "fixed_price", "linear_increase", "random_curve"],
            p=[0.05, 0.05, 0.1, 0.2, 0.3, 0.3]
        )
        self._comp_strategy = CompStrategySimulation(self._comp_strat)
        self._min_action = min_action
        self._action_step = action_step
        self._comp_sellout_price = comp_sellout_price
        self._early_termination_penalty = early_termination_penalty
        self._price_diff_penalty = price_diff_penalty
        self._loadactor_diff_penalty = loadactor_diff_penalty
        self._stock_remainder_penalty = stock_remainder_penalty
        self._our_price = 50
        self._comp_price = 50
        self._last_comp_price = [0]
        self._all_demand = []
        self._print_step = print_step
        
    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec
    
    def current_time_step(self):
        return self._current_time_step

    def reset(self):
        self._current_time_step = self._reset()
        return self._current_time_step

    def step(self, action):
        self._current_time_step = self._step(action)
        return self._current_time_step

    def _reset(self):
        self._episode_ended = False
        self._selling_season += 1
        self._dpc_game.reset()
        self._simulator.reset_environment()
        self._comp_strat = np.random.choice(
            a=["random_ranges", "highstart_randomranges", "follower_strategy", "fixed_price", "linear_increase", "random_curve"],
            p=[0.05, 0.05, 0.1, 0.2, 0.3, 0.3]
        )
        self._comp_strategy = CompStrategySimulation(self._comp_strat)
        self._our_price = 50
        self._comp_price = 50
        self._last_comp_price = [0]
        self._all_demand = []
        return ts.restart(np.array(self._dpc_game.state, dtype=np.int32))

    def _step(self, action):
        
        if self._episode_ended:
            # The last action ended the episode. Ignore the current action and start a new episode.
            return self.reset()
        
        if self._print_step:
            print(f'Taking action step in selling period: {self._dpc_game.state[0]}')
        
        if self._dpc_game.state[0] == 1:
            last_price = 50
        else:
            last_price = self._our_price
        
        # Have the policy take one action step
        action = action.item()
        self._our_price = self._min_action + self._action_step*int(action)
        
        if self._print_step:
            print(f'Action retrieved from policy: {action}, price set to: {self._our_price}')
        
        # Let competitor take a step
        self._comp_price = self._comp_strategy.pick_pricepoint(last_comp_price=self._last_comp_price)
        
        if self._print_step:
            print(f'Competitor will set price set to: {self._comp_price}')
        
        if self._simulator.comp_stock <= 0:
            self._comp_price = self._comp_sellout_price
            if self._print_step:
                print(f'Price of competitor is set to {self._comp_sellout_price}, because it no longer has stock.')
   
        # Run a step in the simulation
        log_period = self._simulator.period
        log_comp_stock = self._simulator.comp_stock > 0
        
        self._our_demand, self._comp_demand = self._simulator.simulate_demand(
            our_price=self._our_price, comp_price=self._comp_price)
        
        if self._print_step:
            print(f'prices returned demand: {self._our_demand}, and competitor demand: {self._comp_demand}')

        self._reward = self._our_demand[0] * self._our_price
        
        if self._print_step:
            print(f'This results in {self._reward} direct revenue')
        
        add_row = {
            'our_strategy': 'dqnagent',
            'competition_id': 'dqnagent' + str(self._selling_season),
            'selling_season': self._selling_season, 
            'selling_period': log_period, 
            'competitor_id': self._comp_strat, 
            'price_competitor': self._comp_price, 
            'price': self._our_price, 
            'demand': self._our_demand[0], 
            'competitor_has_capacity': log_comp_stock, 
            'revenue': self._reward,
        }
        
        # Update states
        vars_dict = {
            'selling_period': self._simulator.period,
            'loadfactor': 80 - self._simulator.our_stock,
            'comp_loadfactor': 80 - self._simulator.comp_stock,
            'competitor_has_capacity': self._simulator.comp_stock > 0,
            'price_competitor_t-1': self._comp_price,
            'price_competitor_t-2': self._dpc_game.price_competitor_t1,
            'price_competitor_t-3': self._dpc_game.price_competitor_t2,
            'price_competitor_t-4': self._dpc_game.price_competitor_t3,
            'price_competitor_t-5': self._dpc_game.price_competitor_t4,
            'price_competitor_t-6': self._dpc_game.price_competitor_t5,
            'price_competitor_t-7': self._dpc_game.price_competitor_t6,
            'price_competitor_t-8': self._dpc_game.price_competitor_t7,
            'price_competitor_t-9': self._dpc_game.price_competitor_t8,
            'price_competitor_t-10': self._dpc_game.price_competitor_t9,
            'price_t-1': self._our_price,
            'price_t-2': self._dpc_game.price_t1,
            'price_t-3': self._dpc_game.price_t2,
            'price_t-4': self._dpc_game.price_t3,
            'price_t-5': self._dpc_game.price_t4,
            'price_t-6': self._dpc_game.price_t5,
            'price_t-7': self._dpc_game.price_t6,
            'price_t-8': self._dpc_game.price_t7,
            'price_t-9': self._dpc_game.price_t8,
            'price_t-10': self._dpc_game.price_t9,
            'demand_t-1': self._our_demand[0],
            'demand_t-2': self._dpc_game.demand_t1,
            'demand_t-3': self._dpc_game.demand_t2,
            'demand_t-4': self._dpc_game.demand_t3,
            'demand_t-5': self._dpc_game.demand_t4,
            'demand_t-6': self._dpc_game.demand_t5,
            'demand_t-7': self._dpc_game.demand_t6,
            'demand_t-8': self._dpc_game.demand_t7,
            'demand_t-9': self._dpc_game.demand_t8,
            'demand_t-10': self._dpc_game.demand_t9,
            'demand_competitor_t-1': self._comp_demand[0],
            'demand_competitor_t-2': self._dpc_game.demand_competitor_t1,
            'demand_competitor_t-3': self._dpc_game.demand_competitor_t2,
            'demand_competitor_t-4': self._dpc_game.demand_competitor_t3,
            'demand_competitor_t-5': self._dpc_game.demand_competitor_t4,
            'demand_competitor_t-6': self._dpc_game.demand_competitor_t5,
            'demand_competitor_t-7': self._dpc_game.demand_competitor_t6,
            'demand_competitor_t-8': self._dpc_game.demand_competitor_t7,
            'demand_competitor_t-9': self._dpc_game.demand_competitor_t8,
            'demand_competitor_t-10': self._dpc_game.demand_competitor_t9,
        }
        
        self._dpc_game.update_state(vars_dict)
        self._dpc_game.update_reward(self._reward)
        
        # Save step and action for the next round
        self._last_comp_price = self._our_price  # Is used in comp strategy, therefore comp price is our price
        self._all_demand.append(self._our_demand[0])
        
        # Make sure episodes don't go on forever.
        if self._dpc_game.state[0] == 100:
            # Add additional penalty for ending the season with high stock left
            self._episode_ended = True
            if self._print_step:
                print('Season finished')
                print(f'Stock remainder penalty is set to: {self._stock_remainder_penalty}')
                print('{} stock left, results in a penalty of: {}'.format(
                    self._simulator.our_stock, self._stock_remainder_penalty * self._simulator.our_stock))
                print('Reward for final step in this episode: {}'.format(
                    self._reward - self._stock_remainder_penalty * self._simulator.our_stock))
            
            final_reward = self._reward - self._stock_remainder_penalty * self._simulator.our_stock
            add_row['reward'] = final_reward
            self._dpc_game.competition_results_df = self._dpc_game.competition_results_df.append(add_row, ignore_index=True)
            return ts.termination(np.array(self._dpc_game.state, dtype=np.int32), final_reward)
        elif self._dpc_game.loadfactor >= 80:
            # Add additional penalty for ending the season early (higher penalty longer in advance)
            self._episode_ended = True
            if self._print_step:
                print('Season finished early, all stock is sold out.')
                print(f'Early termination penalty is set to {self._early_termination_penalty} per day')
                print('There is {} days left, resulting in a penalty of: {}'.format(
                      100 - self._dpc_game.state[0], self._early_termination_penalty * (100 - self._dpc_game.state[0])))
                print('Reward for final step in this episode: {}'.format(
                    self._reward - self._early_termination_penalty * (100 - self._dpc_game.state[0])))
                
            final_reward = self._reward - self._early_termination_penalty * (100 - self._dpc_game.state[0])
            add_row['reward'] = final_reward
            self._dpc_game.competition_results_df = self._dpc_game.competition_results_df.append(add_row, ignore_index=True)
            return ts.termination(np.array(self._dpc_game.state, dtype=np.int32), final_reward)
        else:
            # Add additional penalty for changing prices by a lot
            if self._dpc_game.state[0] == 2:
                price_diff_penal = 0
            else:
                price_diff_penal = abs(self._our_price - last_price)**2 * self._price_diff_penalty
            # Add additional penaly for selling out too quickly
            load_diff = abs(self._dpc_game.loadfactor - (0.8 * self._dpc_game.state[0]))
            load_diff_penalty = load_diff**2 * self._loadactor_diff_penalty
            
            final_reward = self._reward - price_diff_penal - load_diff_penalty
            
            if self._print_step:
                print(f'Transitioning to next step')
                print(f'The penalty for price diff is: {self._price_diff_penalty}, and load diff is: {self._loadactor_diff_penalty}')
                print('The price diff is {}, resulting in a penalty of: {}'.format(
                     abs(self._our_price - last_price), price_diff_penal))
                print('The load diff is {}, resulting in a penalty of: {}'.format(load_diff, load_diff_penalty))
                print(f'Reward for this step: {final_reward}')
                
            add_row['reward'] = final_reward
            self._dpc_game.competition_results_df = self._dpc_game.competition_results_df.append(add_row, ignore_index=True)
            return ts.transition(np.array(self._dpc_game.state, dtype=np.int32), reward=final_reward, discount=self._discount)
        
        
class CreateAirlineSimulation():
    
    def __init__(self, demand_set_price=None, demand_exp_factor=None, price_sensitivity_factor=None, 
                 competitiveness_score=None, our_stock=80, comp_stock=80):
        """
        Class is used to simulate the demand for flight tickets.

        Attributes:
            demand_set_price: Starting/opening price which would result in lambda 1 (~1 demand when prices are all equal)
            demand_exp_factor: Exponential factor that increases the price demand every period
            price_sensitivity_factor: How important pricing is in demand for this season
            competitiveness_score: How importance price difference with competitor is for this season
        """
        self.period = 1
        self.our_stock = our_stock
        self.comp_stock = comp_stock
        self.demand_set_price = demand_set_price
        self.demand_exp_factor = demand_exp_factor
        self.price_sensitivity_factor = price_sensitivity_factor
        self.competitiveness_score = competitiveness_score
        self.demand_curve_prices = []
        self._initialize_demand_curve()
    
    def _initialize_demand_curve(self):
        """
        Initialize demand curve and environment characteristics.
        """
        
        if self.demand_set_price is None:
            self.demand_set_price = np.random.normal(50, 10)
            
        if self.demand_exp_factor is None:
            self.demand_exp_factor = np.random.normal(1.005, 0.001)
            
        if self.price_sensitivity_factor is None:
            self.price_sensitivity_factor = np.random.normal(1.1, 0.05)
            
        if self.competitiveness_score is None:
            self.competitiveness_score = np.random.normal(1.1, 0.05)
        
        self.demand_curve_prices = np.array([
            self.exp_increase(self.demand_set_price, self.demand_exp_factor, x) for x in range(1, 101)
        ])
    
    @staticmethod
    def exp_increase(start_point, exp_inc, timestep):
        """
        Calculates exponential increase based on timestep.
        """
        return start_point * exp_inc**(timestep-1)
    
    @staticmethod
    def calculate_lambdas(demand_set_price, our_price, comp_price, price_sensitivity_factor, competitiveness_score):
        """
        Given your price, and the price of competitor, you will pull demand from a certain distribution.
        The distribution is a poisson distribution which uses lambda as input to determine the distribution.

        Lambda must be a relative score depending on:
        Our prices relative to demand curve
        Our price relative to competition
        Price sensitivity of market (price elastivity)
        Competitiveness of the market
        """

        # Set lambda based on price diff with set price
        our_lambda = 1 + (demand_set_price - our_price) / our_price
        comp_lambda = 1 + (demand_set_price - comp_price) / comp_price

        # Adjust for price sensitivity
        if our_price > demand_set_price:
            our_lambda = our_lambda / price_sensitivity_factor
        else:
            our_lambda = our_lambda * price_sensitivity_factor

        if comp_price > demand_set_price:
            comp_lambda = comp_lambda / price_sensitivity_factor
        else:
            comp_lambda = comp_lambda * price_sensitivity_factor

        # Adjust for price difference and how competitive this market is
        if our_price > comp_price:
            our_lambda = our_lambda / (1 + (our_price - comp_price) / comp_price) / competitiveness_score
            comp_lambda = comp_lambda / (1 + (comp_price - our_price) / our_price) * competitiveness_score
        else:
            our_lambda = our_lambda / (1 + (our_price - comp_price) / comp_price) * competitiveness_score
            comp_lambda = comp_lambda / (1 + (comp_price - our_price) / our_price) / competitiveness_score

        return our_lambda, comp_lambda
    
    def simulate_demand(self, our_price, comp_price):
        """
        Use our price and price of competitor to simulate demand
        Checks demand with current stock and returns demand
        """
        # Create lambdas to define the distribution from which the demand will be picked
        our_lambda, comp_lambda = self.calculate_lambdas(
            self.demand_set_price, our_price, comp_price, self.price_sensitivity_factor, self.competitiveness_score
        )
        
        # Pick the actual demand
        our_demand = np.random.poisson(lam=our_lambda, size=1)
        comp_demand = np.random.poisson(lam=comp_lambda, size=1)
        
        # Check if demand can be met, i.e. there is stock left
        if our_demand > self.our_stock:
            our_demand = [self.our_stock]
            
        if comp_demand > self.comp_stock:
            comp_demand = [self.comp_stock]
            
        self.update_environment(our_demand, comp_demand)
        
        return our_demand, comp_demand
    
    def update_environment(self, our_demand, comp_demand):
        """
        Update environment variables to be ready for next period simulation.
        """
        
        # reset if simulation finished
        if self.period == 100:
            self.reset_environment()
        # Update period, stock and set price otherwise
        else:
            self.period += 1
            self.our_stock -= our_demand[0]
            self.comp_stock -= comp_demand[0]
            self.demand_set_price = self.demand_curve_prices[self.period-1]
            
    def reset_environment(self):
        self.period = 1
        self.our_stock = 80
        self.comp_stock = 80
        self.demand_set_price=None
        self.demand_exp_factor=None
        self.price_sensitivity_factor=None 
        self.competitiveness_score=None
        self._initialize_demand_curve()
        
        
# Create custom policy
class CustomOurStrategyPolicy(tf_policy.TFPolicy):
    
    def __init__(self, time_step_spec, action_spec, policy_state_spec):
        self._time_step_spec = time_step_spec
        self._action_spec = action_spec
        self._policy_state_spec = policy_state_spec
        self.exp1, self.exp2 = np.nan, np.nan
        self.begin, self.end = np.nan, np.nan
        self.price_points = []
        self.rc_precalc_price_path()
        
        super(CustomOurStrategyPolicy, self).__init__(
            time_step_spec=time_step_spec,
            action_spec=action_spec
        )
        
    def _action(self, time_step, policy_state, seed):
        
        selling_period = time_step.observation[0][0]
        price = tf.gather(self.price_points, selling_period-1)
        action = tf.cast([round((np.clip(price, 30, 150) - 30) / 3)], dtype=tf.int32)
        
        return PolicyStep(action, policy_state)
    
    def reset(self, policy_state=None):
        
        self.rc_precalc_price_path()
    
    def rc_precalc_price_path(self):
        self.exp1 = np.random.normal(1.02, 0.015)
        self.exp2 = np.random.normal(1.02, 0.015)
        self.begin = np.random.normal(50, 10)
        self.end = np.random.normal(100, 10)
        self.price_points = tf.constant(self.create_scaled_polynomial_curve(self.begin, self.end, 100, self.exp1, self.exp2))
    
    @staticmethod
    def polynomial_increase(start_point, factor1, factor2, timestep):
        return start_point + factor1**timestep - factor2**(100-timestep)

    @staticmethod
    def create_scaled_polynomial_curve(start_point, endpoint, dbd_range, factor1, factor2):
        initial_curve = [
            CustomOurStrategyPolicy.polynomial_increase(start_point, factor1, factor2, x) for x in range(dbd_range)
        ]
        second_curve = [x + start_point - min(initial_curve) for x in initial_curve]
        third_curve = [x / (max(second_curve) / endpoint) for x in second_curve]

        return third_curve
    
    
class OurStrategySimulation():
    """
    Use baseline strategies to use as our prices in simulations.
    Pick either 'fixed_price' as the always 50 stragegy,
    'linear_increase' as the gradually increasing price from e.g. 30-80 or 40-70,
    or the 'linear_demand', in which the demand is used to increase or decrease prices
    to try and fill the loadfactor linearly over time.
    """
    
    def __init__(self, strategy, start_price, end_price=None):
        self.strategy = strategy
        self.stock = 80
        self.period = 1
        self.price = start_price
        self.start_price = start_price
        self.end_price = end_price
        self.hist_demand = []
        self.comp_has_capacity = True
        
    def pick_pricepoint(self, last_demand, comp_has_capacity):
        """
        Use the chosen strategy to return a price point for the current period.
        """
        if self.strategy == 'fixed_price':
            return_price = self.price
            self.update_environment(return_price, last_demand)
            return return_price
        elif self.strategy == 'linear_increase':
            return_price = self.start_price + (self.end_price - self.start_price) / 100 * self.period
            self.update_environment(return_price, last_demand)
            return return_price
        elif self.strategy == 'linear_demand':
            if self.period == 1:
                return_price = self.start_price
                self.update_environment(return_price, last_demand)
                return return_price
            else:
                # Update demand and stock
                current_stock = self.stock - last_demand
                all_demand = self.hist_demand + [last_demand]
                
                # Calculate what stock should be for linear loadfactor
                planned_stock = 80 - self.period * 0.8
                
                # Calculate recent demand
                avg_demand = sum(all_demand[-3:]) / len(all_demand[-3:])
                
                # If we are going to slow, decrease price (but not if we are already selling much recently)
                if (planned_stock < current_stock) & (avg_demand < 2.0):
                    return_price = self.price - 2
                # If we are going to fast, increase price (but not if we are not selling recently anyway)
                elif (planned_stock > current_stock) & (avg_demand > 0.5):
                    return_price = self.price + 2
                else:
                    return_price = self.price
                    
                if (self.comp_has_capacity is True) & (comp_has_capacity is False):
                    return_price += 5
                    
                self.update_environment(return_price, last_demand)
                return return_price
        else:
            raise ValueError('Strategy should be either of ["fixed_price", "linear_increase", "linear_demand"]')
    
    def update_environment(self, return_price, last_demand):
        """
        Update environment variables to be ready for next period simulation.
        """
        # reset if simulation finished
        if self.period == 100:
            self.period = 1
            self.stock = 80
            self.price = self.start_price
            self.hist_demand = []
            self.comp_has_capacity = True
        else:
            # update env variables otherwise
            self.period += 1  
            self.stock -= last_demand
            self.price = return_price
            self.comp_has_capacity = True
            self.hist_demand.append(last_demand)


class CompStrategySimulation():
    """
    Competitor stratagies that have been seen and are relatively easy to implement.c
    'follower_strategy' wil start with a random price for the first 10 periods, 
    then use the price we set 2 days ago, 'random_ranges' will always pick a random price
    between a higher and lower bound, and 'highstart_randomranges' will start with a high price (e.g. 100)
    and then lower after an x number of days to move between boundaries.
    """
    
    def __init__(self, strategy):
        self.strategy = strategy
        self.period = 1
        self.lower_bound = np.random.randint(40, 60)
        self.upper_bound = np.random.randint(60, 90)
        self.fixed_price = np.random.randint(40, 80)
        self.hist_comp_price = []
        self.high_start_nr_days = None
        self.exp1, self.exp2 = np.nan, np.nan
        self.begin, self.end = np.nan, np.nan
        self.price_points = []
        
    def pick_pricepoint(self, last_comp_price):
        """
        Use the chosen strategy to return a price point for the current period.
        """
        if self.strategy == 'random_ranges':
            return_price = np.random.randint(self.lower_bound, self.upper_bound)
            self.update_environment(last_comp_price)
            return return_price
        elif self.strategy == 'highstart_randomranges':
            if self.period == 1:
                self.high_start_nr_days = np.random.randint(25, 50)
                return_price = 100
                self.update_environment(last_comp_price)
                return return_price
            elif self.period >= self.high_start_nr_days:
                return_price = np.random.randint(self.lower_bound, self.upper_bound)
                self.update_environment(last_comp_price)
                return return_price
            else:
                return_price = 100
                self.update_environment(last_comp_price)
                return return_price
        elif self.strategy == 'follower_strategy':
            if self.period <= 10:
                return_price = np.random.randint(self.lower_bound, self.upper_bound)
                self.update_environment(last_comp_price)
                return return_price
            else:
                return_price = self.hist_comp_price[-2]
                self.update_environment(last_comp_price)
                return return_price
        elif self.strategy == 'fixed_price':
            return_price = self.fixed_price
            self.update_environment(last_comp_price)
            return return_price
        elif self.strategy == 'linear_increase':
            return_price = self.lower_bound + (self.upper_bound - self.lower_bound) / 100 * self.period
            self.update_environment(return_price)
            return return_price
        elif self.strategy == 'random_curve':
            if self.period == 1:
                self.rc_precalc_price_path()
            return_price = self.price_points[self.period]
            self.update_environment(last_comp_price)
            return return_price
        else:
            raise ValueError('Strategy should be either of ['
                             '"follower_strategy", "random_ranges", "highstart_randomranges", '
                             '"fixed_price", "linear_increase", "random_curve"'
                             ']')
            
    def update_environment(self, last_comp_price):
        """
        Update environment variables to be ready for next period simulation.
        """
        # reset if simulation finished
        if self.period == 100:
            self.period = 1
            self.lower_bound = np.random.randint(40, 60)
            self.upper_bound = np.random.randint(60, 90)
            self.fixed_price = np.random.randint(40, 80)
            self.hist_comp_price = []
            self.high_start_nr_days = None
        else:
            # update env variables otherwise
            self.period += 1  
            self.hist_comp_price.append(last_comp_price)
            
    def rc_precalc_price_path(self):
        self.exp1 = np.random.normal(1.02, 0.015)
        self.exp2 = np.random.normal(1.02, 0.015)
        self.begin = np.random.normal(60, 10)
        self.end = np.random.normal(100, 10)
        self.price_points = tf.constant(self.create_scaled_polynomial_curve(self.begin, self.end, 100, self.exp1, self.exp2))
    
    @staticmethod
    def polynomial_increase(start_point, factor1, factor2, timestep):
        return start_point + factor1**timestep - factor2**(100-timestep)

    @staticmethod
    def create_scaled_polynomial_curve(start_point, endpoint, dbd_range, factor1, factor2):
        initial_curve = [
            CustomOurStrategyPolicy.polynomial_increase(start_point, factor1, factor2, x) for x in range(dbd_range)
        ]
        second_curve = [x + start_point - min(initial_curve) for x in initial_curve]
        third_curve = [x / (max(second_curve) / endpoint) for x in second_curve]

        return third_curve
