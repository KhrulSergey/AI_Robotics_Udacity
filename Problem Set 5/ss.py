def cte(self, radius):
    cte = 0.0
    if self.x &lt; radius:
        distance = sqrt((abs(self.x - radius)**2) + abs((self.y - radius)**2))
        if distance &lt; radius:
            cte = -distance
        else:
            cte = distance - radius
    elif self.x &gt; 3*radius:
        distance = sqrt((abs(self.x - 3*radius)**2) + abs((self.y - radius)**2))
        if distance &lt; radius:
            cte = -distance
        else:
            cte = distance - radius
    elif self.y &gt; radius:
        cte = self.y - 2*radius
    else:
        cte = -self.y

    return cte


def cte(self, radius):



return err