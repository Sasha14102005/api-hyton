package main
import (
	"github.com/gin-gonic/gin"
)

type Cat struct {
	Name string `json:"name"`
	TailLength int `json:"tail_length"`
	IsStrip bool `json:"is_strip"`

}

func main() {
	r := gin.Default()

    r.GET("/cat", func (c *gin.Context) {

        cat := &Cat{
			Name: "Курт",
			TailLength: 25,
			IsStrip: true,
		}

		c.JSON(200, cat)
	})

	r.Run("0.0.0.0:8888")
}