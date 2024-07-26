import streamlit as st

def max_problems_solved(N, P):
    total_time = 240  # 4 hours in minutes
    avail_time = total_time - P
    
    if avail_time <= 0:
        return 0
    problems_solved = 0
    time_spent = 0
    for a in range(1, N + 1):
        time_required = 5 * a
        if time_spent + time_required <= avail_time:
            problems_solved += 1
            time_spent += time_required
        else:
            break
    return problems_solved
def main():
    st.title("Diwali Contest Problem Solver")
    N = st.number_input("Enter the number of problems:", min_value=1, step=1)
    P = st.number_input("Enter the travel time in minutes:", min_value=0, step=1)

    if st.button("Calculate"):
        result = max_problems_solved(N, P)
        st.write(f"Max can solve {result} problem(s).")

if __name__ == "__main__":
    main()

