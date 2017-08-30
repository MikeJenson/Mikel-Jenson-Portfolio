function love.load()
	player = {}
	player.x = 400
	player.y = 600
	player.bullets = {}
	player.cooldown = 20
	player.speed = 10
	player.fire = function()
		if player.cooldown <= 0 then
			player.cooldown = 20
			bullet = {}
			bullet.x = player.x - 5
			bullet.y = player.y - 55
			table.insert(player.bullets, bullet)
		end
	end
end

function love.update(dt)
	player.cooldown = player.cooldown -1
	if love.keyboard.isDown("right") then
		player.x = player.x + player.speed
	elseif love.keyboard.isDown("left") then
		player.x = player.x - player.speed
	end

	if love.keyboard.isDown("space") then
		player.fire()
	end

	for i,v in ipairs(player.bullets) do
		if v.y < -10 then
			table.remove(player.bullets, i)
		end
		v.y = v.y - 10
	end
end

function love.draw()
	love.graphics.setColor(255, 100, 100)
	love.graphics.circle('fill', player.x, player.y, 50, 50)
	love.graphics.setColor(0, 255, 50)
	for _,v in pairs(player.bullets) do
		love.graphics.rectangle("fill", v.x, v.y, 10, 10)
	end
end
