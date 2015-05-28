class MSM:
   def __init__(self,T):
      self.T=T
      self._pi = None
   @property
      def pi(self):
         if self._pi = None:
            self._pi = get_pi(self.T)
         return self._pi
