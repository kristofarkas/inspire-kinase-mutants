from radical.htbac import Esmacs, Runner

muts = ['nilotinib-e255k']

ht = Runner()
esm = Esmacs(number_of_replicas=25, systems=muts, rootdir='../../models', full=True, cores=16, cutoff=10, water_model='tip4')

ht.add_protocol(esm)

ht.rabbitmq_config(hostname='openshift-node1.ccs.ornl.gov', port=30673)
ht.run(walltime=720)
