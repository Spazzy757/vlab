package health

import (
	"database/sql"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CheckHandler(db *sql.DB) gin.HandlerFunc {
	return func(ctx *gin.Context) {
		isHealthy := true

		if err := db.PingContext(ctx); err != nil {
			isHealthy = false
		}

		ctx.JSON(http.StatusOK, gin.H{
			"healthy": isHealthy,
			"dependencies": []gin.H{
				{
					"name":    "cockroachdb",
					"healthy": isHealthy,
				},
			},
		})
	}
}
