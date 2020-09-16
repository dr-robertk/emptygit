from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

comm.barrier()
for i in range(0,4):
    if(i == rank):
        print("Hello World! I'm rank ", rank," out of ",nprocs,".",flush=True)
    comm.barrier()
maxRank = comm.allreduce( rank, op=MPI.MAX )
if( rank == 0 ):
    print('Max rank is ',maxRank)

