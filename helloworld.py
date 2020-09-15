from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

print("Hello World! I'm rank ", rank," out of ",nprocs,".")
