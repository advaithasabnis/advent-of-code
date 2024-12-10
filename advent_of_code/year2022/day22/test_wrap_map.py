from .shared import Net


# These are the 11 possible nets of a cube
patterns = """
####
####
####
####
################
################
################
################
####
####
####
####

   ###
   ###
   ###
############
############
############
###
###
###

      ###
      ###
      ###
############
############
############
###
###
###

         ###
         ###
         ###
############
############
############
###
###
###

   ###
   ###
   ###
############
############
############
   ###
   ###
   ###

      ###
      ###
      ###
############
############
############
   ###
   ###
   ###

#########
#########
#########
      #########
      #########
      #########

######
######
######
   #########
   #########
   #########
      ###
      ###
      ###

######
######
######
   #########
   #########
   #########
         ###
         ###
         ###

      ###
      ###
      ###
#########
#########
#########
      ######
      ######
      ######

######
######
######
   ######
   ######
   ######
      ######
      ######
      ######
""".strip(
    '\n'
)


def parse_pattern(text: str):
    bounds = set()
    rows = text.split('\n')
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '#':
                bounds.add(complex(x, y))

    return bounds


def test_interior_exterior():
    """
    Test that number of interior and exterior points is correct.
    Number of exterior points minus number of interior points is always 4 for nets of a cube.
    """
    for pattern in patterns.split('\n\n'):
        bounds = parse_pattern(pattern)
        net = Net(bounds, is_cube=True)

        int_corners = sum(1 if net.is_interior_corner(pos) else 0 for pos in net.bounds)
        ext_corners = sum(1 if net.is_exterior_corner(pos) else 0 for pos in net.bounds)

        assert ext_corners - int_corners == 4


def test_cube_wrap_map():
    """Test that mapping exists for all valid outer positions in a cube"""
    for pattern in patterns.split('\n\n'):
        bounds = parse_pattern(pattern)
        net = Net(bounds, is_cube=True)

        assert len(net.wrap_map) / 14 == net.face_length


def test_2d_wrap_map():
    """Test that mapping exists for all valid outer positions in a 2d shape"""
    for pattern in patterns.split('\n\n'):
        bounds = parse_pattern(pattern)
        net = Net(bounds, is_cube=False)

        assert len(net.wrap_map) / 14 == net.face_length
