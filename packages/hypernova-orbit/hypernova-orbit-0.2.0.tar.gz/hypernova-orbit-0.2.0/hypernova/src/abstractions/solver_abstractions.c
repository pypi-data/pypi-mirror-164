#include "solver_abstractions.h"

void free_solver_solution(SolverSolution *solution)
{
    free(solution->t);
    free(solution->jd);
    free(solution->y);
    free(solution);
}

Solver cast_to_solver(void *solver)
{
    return *(Solver *)solver;
}