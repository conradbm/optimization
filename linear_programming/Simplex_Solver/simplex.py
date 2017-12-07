"""
An LP_MODEL class object is meant to be a constructive, robust, and flexible
linear model solver from file IO to solution.

Example employment is as follows:

lpSolver = LP_MODEL(<absolutePath | relativePath>, <debug>)
lpSolver._solution # int or double
lpSolver._optimalVariables #list or dictionary

"""

class LP_MODEL:
    
    # Class attributes (I.e., built inside of the class, accessible outside)
    _model_path=""
    _raw_model_list=[]
    _debug=False
    
    # File reader helper function.
    #
    # File structure example.
    #
    # E.g.,.
    #    max x1+2*x2
    #    s.t
    #    3*x1+4*x2<=5
    #    2*x1<=3
    #    x1>=0
    #    x2>=0
    #
    def read_model_file(self):
        if self._debug:
            print("Parsing path:", self._model_path)
        if(self._model_path!=""):
            lines=[]
            with open(self._model_path, "r") as file_in:
                for line in file_in.readlines():
                    lines.append(line.rstrip())
            return lines

    # Constructor.
    # Optional Parameters:
    #    1. path
    #    2. debug
    #
    # ___________________________________
    # ____________ Logic Map ____________
    # ___________________________________
    #
    #   1. File IO.
    #   2. Parse raw_model_input into necessary structures.
    #   3. Update structures (with new variables/coeffs).
    #   4. Merge data structures into Panda Tableau.
    #   5. Build and apply functions to reduce the tableau.
    #   6. Respond with results.
    #
    def __init__(self, path="", debug=False):
        self._debug=debug
        if path=="":
            if self._debug:
                print("No initial model supplied.")

        else:
            if self._debug:
                print("Path successfully acquired.")

            self._model_path=path
            self._raw_model_list=self.read_model_file()

        if self._debug:
            print("Constructed.")
            print(self._raw_model_list)

# the path isn't absolute, but it assumes we're in the same directory
lpSolver = LP_MODEL("p1.txt")
print(lpSolver._raw_model_list)
