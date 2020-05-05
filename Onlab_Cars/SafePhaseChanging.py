import traci


def ChangeToDesiredPhase(tls, current_phase, desired_phase, state_of_change, time_passed_since_switch):
    if current_phase == desired_phase or 20 >= time_passed_since_switch:
        print("Nothing happened")
        return time_passed_since_switch, state_of_change

    print("!!!!!!\nPhase change in progress:")
    print("current phase:", current_phase)
    print("desired phase:", desired_phase)
    print("state of change:", state_of_change, "\n")

    if state_of_change == 0:
        traci.trafficlight.setPhase(tlsID=tls, index=current_phase + 1)
        state_of_change += 1
        print("Setting state to yellow! State of Change:", state_of_change)
        return time_passed_since_switch, state_of_change

    elif 1 <= state_of_change < 1 + 2:  # traci.trafficlight.getPhaseDuration(tls):
        state_of_change += 1
        print("Yellow state!")
        return time_passed_since_switch, state_of_change

    elif state_of_change == 1 + 2:
        traci.trafficlight.setPhase(tlsID=tls, index=desired_phase)
        print("Phase Change successful!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:", desired_phase)
        state_of_change = 0
        # time_passed_since_switch = 0
        return time_passed_since_switch, state_of_change

    else:
        return state_of_change  # current state is good
