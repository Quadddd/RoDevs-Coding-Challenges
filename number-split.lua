local t = tostring
local function f(n)
	n = t(n)
	local x = { }
	for i, v in pairs(n:split('')) do
		table.insert(x, v .. ('0'):rep(#n:sub(i, #n)-1))
	end
	return table.concat(x, ' + ')
end
