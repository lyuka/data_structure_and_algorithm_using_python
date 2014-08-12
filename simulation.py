# Implementaion of the main simulation class.
from myarray import myArray
from llistqueue import Queue
from simpeople import TicketAgent, Passenger

class TicketCounterSimulation:
    # Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        self._psgArrTimeList = random.sample( range(numMinutes), int(self._arriveProb * numMinutes) )

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = myArray( numAgents )
        for i in range( numAgents ):
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes):
            self._handleArrive( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    # Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print ''
        print 'Number of passengers served = %d ' % numServed
        print 'Number of passengers remaining in line = %d ' % len(self._passengerQ)
        print 'The average wait time was %4.2f minutes. ' % avgWait

    # The help function used in run.
    def _handleArrive( self, curTime ):  # Handles simulation rule 1
        if curTime in self._psgArrTimeList:
            cur_psg = Passenger( self._numPassengers + 1, curTime )
            #print 'Time %4d : Passenger %d arrived.' % (curTime, cur_psg.idNum())
            self._passengerQ.enqueue( cur_psg )
            self._numPassengers += 1

    def _handleBeginService( self, curTime ):  # Handles simulation rule 2
        if len(self._passengerQ):
            for i in range(len(self._theAgents)):
                if self._theAgents[i].isFree():
                    cur_psg = self._passengerQ.dequeue()
                    #print 'Time %4d : Agent %d Started serving passenger %d.' % (curTime, self._theAgents[i].idNum(), cur_psg.idNum())
                    self._theAgents[i].startService(cur_psg, curTime + self._serviceTime)
                    self._totalWaitTime += ( curTime - cur_psg.timeArrived() )
                    break
            

    def _handleEndService( self, curTime ):  # Handles simulation rule 3
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFinished( curTime ):
                cur_psg = self._theAgents[i].stopService()
                #print 'Time %4d : Agent %d Stoped serving passenger %d.' % (curTime, self._theAgents[i].idNum(), cur_psg.idNum())
                


if __name__ == '__main__':
    import random
    
    numAgents = input('Number of ticket agents: ')
    numMinutes = input('Number of minutes to simulate: ')
    serviceTime = input('Average service time per passenger: ')
    betweenTime = input('Average time between passenger arrival: ')

    random.seed( 4500 )
    a_simu = TicketCounterSimulation( numAgents, numMinutes, betweenTime, serviceTime )
    a_simu.run()
    a_simu.printResults()
    
